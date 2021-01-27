from ..utils import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from marshmallow_enum import EnumField
import enum

class EventCategory(enum.Enum):
    conference = "conference"
    seminar = "seminar"
    congress = "congress"
    course = "course"

class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    category = db.Column(db.Enum(EventCategory), nullable=False, server_default="conference")
    begin_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    virtual = db.Column(db.Boolean, nullable=False, default=True)
    owner = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class EventSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Event
        sqla_session = db.session

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    category = EnumField(required=True,
                         enum=EventCategory)
    begin_date = fields.DateTime(format="%d/%m/%Y", required=True)
    end_date = fields.DateTime(format="%d/%m/%Y", required=True)
    address = fields.String(required=True)
    virtual = fields.Boolean(required=True)
    owner = fields.Integer(required=True)