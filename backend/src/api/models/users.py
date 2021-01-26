from ..utils import db
import enum
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .events import EventSchema

class Role(enum.Enum):
    admin = "admin"
    promoter = "promoter"

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.Enum(Role), server_default=Role.promoter)
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
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, _hash):
        return sha256.verify(password, _hash)

class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = User
        sqla_session = db.session

    id = fields.Integer(dump_only=True)
    email = fields.Email(required=True)
    events = fields.Nested(
        EventSchema,
        many=True,
        only=[
            "id", "name", "category",
            "begin_date", "end_date"
        ]
    )