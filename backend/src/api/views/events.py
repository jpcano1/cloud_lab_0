from flask_restful import Resource
from flask import request
from ..utils import response_with, responses
from ..utils import db
from flask_jwt_extended import jwt_required, get_jwt_identity

from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

# Models
from ..models import Event as EventModel
from ..models import EventSchema

import copy

from datetime import datetime

class EventDetail(Resource):
    @jwt_required
    def get(self, event_id):
        owner_id = get_jwt_identity()
        fetched = EventModel.query.filter_by(
            id=event_id, owner=owner_id
        ).first()

        if not fetched:
            return response_with(responses.SERVER_ERROR_404, value={
                "error_message": "Resource does not exists"
            })
        event_schema = EventSchema()
        event = event_schema.dump(fetched)
        return response_with(responses.SUCCESS_200, value={
            "event": event
        })

    @jwt_required
    def put(self, event_id):
        data = request.get_json()

        owner_id = get_jwt_identity()
        fetched = EventModel.query.filter_by(
            id=event_id, owner=owner_id
        ).first()

        if not fetched:
            return response_with(responses.SERVER_ERROR_404, value={
                "error_message": "Resource does not exists"
            })
        try:
            fetched.name = data["name"]
            fetched.category = data["category"]
            fetched.begin_date = datetime.strptime(data["begin_date"], "%d/%m/%Y")
            fetched.end_date = datetime.strptime(data["end_date"], "%d/%m/%Y")
            fetched.address = data["address"]
            fetched.virtual = data["virtual"]
        except KeyError:
            return response_with(responses.INVALID_INPUT_422, value={
                "error_message": "Data incomplete, use PATCH instead"
            })
        except ValueError:
            return response_with(responses.INVALID_INPUT_422, value={
                "error_message": "Please, use valid date ranges"
            })
        db.session.add(fetched)
        db.session.commit()
        event_schema = EventSchema()
        event = event_schema.dump(fetched)
        return response_with(responses.SUCCESS_200, value={
            "event": event
        })

    @jwt_required
    def patch(self, event_id):
        data = request.get_json()

        owner_id = get_jwt_identity()
        fetched = EventModel.query.filter_by(
            id=event_id, owner=owner_id
        ).first()

        if not fetched:
            return response_with(responses.SERVER_ERROR_404, value={
                "error_message": "Resource does not exists"
            })
        fetched_copy = copy.copy(fetched)

        fetched.name = data.get("name", fetched_copy.name)
        fetched.category = data.get("category", fetched_copy.category)
        if data.get("begin_date"):
            fetched.begin_date = datetime.strptime(data["begin_date"], "%d/%m/%Y")
        if data.get("end_date"):
            fetched.begin_date = datetime.strptime(data["end_date"], "%d/%m/%Y")
        fetched.address = data.get("address", fetched_copy.address)
        fetched.virtual = data.get("virtual", fetched_copy.virtual)

        del fetched_copy

        db.session.add(fetched)
        db.session.commit()

        event_schema = EventSchema()
        event = event_schema.dump(fetched)
        return response_with(responses.SUCCESS_200, value={
            "event": event
        })

    @jwt_required
    def delete(self, event_id):
        owner_id = get_jwt_identity()
        fetched = EventModel.query.filter_by(
            id=event_id, owner=owner_id
        ).first()

        if not fetched:
            return response_with(responses.SERVER_ERROR_404, value={
                "error_message": "Resource does not exists"
            })
        db.session.delete(fetched)
        db.session.commit()
        return response_with(responses.SUCCESS_204)

class Event(Resource):
    @jwt_required
    def get(self):
        owner_id = get_jwt_identity()
        fetched = EventModel.query.filter_by(owner=owner_id)
        event_schema = EventSchema(many=True)
        events = event_schema.dump(fetched)
        return response_with(responses.SUCCESS_200, value={
            "events": events
        })

    @jwt_required
    def post(self):
        owner_id = get_jwt_identity()
        data = request.get_json()

        data["owner"] = owner_id
        event_schema = EventSchema()
        try:
            event = event_schema.load(data, session=db.session)
            result = event_schema.dump(event.create())
        except ValidationError as e:
            return response_with(responses.INVALID_INPUT_422, value={
                "error_message": e.messages
            })
        except IntegrityError:
            return response_with(responses.INVALID_INPUT_422, value={
                "error_message": "This conference already exists"
            })
        return response_with(responses.SUCCESS_201, value={
            "event": result
        })