from flask_restful import Resource
from ..models import User as UserModel
from flask import request
from ..models import UserSchema
from ..utils import db, responses, response_with
from sqlalchemy.exc import IntegrityError

class User(Resource):
    def get(self):
        fetched = UserModel.query.all()
        user_schema = UserSchema(many=True)
        users = user_schema.dump(fetched)
        return response_with(responses.SUCCESS_200, value={
            "users": users
        })

    def post(self):
        data = request.get_json()
        if not data.get("password"):
            return response_with(responses.INVALID_INPUT_422, value={
                "error_message": "No password sent"
            })
        data["password"] = UserModel.generate_hash(data["password"])
        user_schema = UserSchema()
        user = user_schema.load(data, session=db.session)
        try:
            user.create()
        except IntegrityError:
            return response_with(responses.INVALID_INPUT_422, value={
                "error_message": "Email already exists"
            })
        except Exception as e:
            return response_with(responses.INVALID_INPUT_422, value={
                "error_message": str(e)
            })
        return response_with(responses.SUCCESS_201, value={
            "message": "User Created"
        })

class UserDetail(Resource):
    def get(self, user_id):
        fetched = UserModel.query.get_or_404(user_id)
        user_schema = UserSchema(only=["id", "email"])
        user = user_schema.dump(fetched)
        return response_with(responses.SUCCESS_200, value={
            "user": user
        })