from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ..models import User as UserModel
from flask import request
from ..models import UserSchema
from ..utils import db, responses, response_with
from sqlalchemy.exc import IntegrityError
from datetime import timedelta

class SignUp(Resource):
    def post(self):
        data = request.get_json()
        if not data.get("password") or not data.get("email"):
            return response_with(responses.INVALID_INPUT_422, value={
                "error_message": "No email or password sent"
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

class LogIn(Resource):
    def post(self):
        data = request.get_json()
        current_user = UserModel.find_by_email(data["email"])

        if not current_user:
            return response_with(responses.INVALID_INPUT_422, value={
                "error_message": "Wrong email or password"
            })
        verification = UserModel.verify_hash(current_user.password,
                                             data["password"])
        if not verification:
            return response_with(responses.UNAUTHORIZED_401, value={
                "error_message": "Wrong email or password"
            })
        expires = timedelta(hours=2)
        access_token = create_access_token(
            identity=str(current_user.id),
            expires_delta=expires
        )
        return response_with(responses.SUCCESS_200, value={
            "access_token": access_token,
            "message": f"Logged in as {current_user.email}"
        })

class UserDetail(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        fetched = UserModel.query.get_or_404(user_id)
        user_schema = UserSchema()
        user = user_schema.dump(fetched)
        return response_with(responses.SUCCESS_200, value={
            "user": user
        })