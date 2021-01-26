from flask_restful import Resource
from ..models import User as UserModel
from flask import request
from ..models import UserSchema
from ..utils import db, responses, response_with

class User(Resource):
    def post(self):
        data = request.get_json()
        data["password"] = UserModel.generate_hash(data["password"])
        user_schema = UserSchema()
        user = user_schema.load(data, session=db.session)
        user.create()
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