from flask_restful import Resource
from ..utils import response_with, responses

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
        pass

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
        pass
