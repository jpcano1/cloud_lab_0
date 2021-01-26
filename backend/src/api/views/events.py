from flask_restful import Resource
from flask import request
from ..utils import response_with, responses
from ..utils import db

from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

# Models
from ..models import Event as EventModel
from ..models import EventSchema

class EventDetail(Resource):
    def get(self, event_id):
        fetched = EventModel.query.get_or_404(event_id)
        event_schema = EventSchema()
        event = event_schema.dump(fetched)
        return response_with(responses.SUCCESS_200, value={
            "event": event
        })

    def put(self, event_id):
        data = request.get_json()
        fetched = EventModel.query.get_or_404(event_id)
        fetched = data
        db.session.add(fetched)
        db.session.commit()
        event_schema = EventSchema()
        event = event_schema.dump(fetched)
        return response_with(responses.SUCCESS_200, value={
            "event": event
        })

    def patch(self, event_id):
        return response_with(responses.SUCCESS_200)

    def delete(self, event_id):
        pass

class Event(Resource):
    def get(self):
        fetched = EventModel.query.all()
        event_schema = EventSchema(many=True)
        events = event_schema.dump(fetched)
        return response_with(responses.SUCCESS_200, value={
            "events": events
        })

    def post(self):
        data = request.get_json()
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