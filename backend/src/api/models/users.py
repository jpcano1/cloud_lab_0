from ..utils import db
from flask_bcrypt import generate_password_hash, check_password_hash
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .events import EventSchema

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    # is_verified = db.Column(db.Boolean, nullable=False, default=False)
    events = db.relationship("Event", backref="User", cascade="all, delete-orphan")

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @staticmethod
    def generate_hash(password):
        return generate_password_hash(password).decode("utf-8")

    @staticmethod
    def verify_hash(hash_, password):
        return check_password_hash(hash_, password)

class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = User
        sqla_session = db.session

    id = fields.Integer(dump_only=True)
    email = fields.Email(required=True)
    password = fields.String(load_only=True, required=True)
    events = fields.Nested(
        EventSchema,
        many=True,
        only=[
            "id", "name", "category",
            "begin_date", "end_date"
        ]
    )