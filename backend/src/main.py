from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors.extension import CORS
from flask_restful import Api
from .api.utils import db
from dotenv import load_dotenv, find_dotenv
from .api.config import (
    DevelopmentConfig,
    ProductionConfig,
    TestingConfig
)
import os, sys
import logging
from .api.views import (Event, EventDetail,
                        SignUp, UserDetail, LogIn)
from flask_jwt_extended import JWTManager

logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s|%(levelname)s|%(filename)s: %(lineno)s| %(message)s",
    level=logging.DEBUG
)

load_dotenv(find_dotenv())

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

if os.getenv("WORK_ENV") == "PROD":
    app_config = ProductionConfig
elif os.getenv("WORK_ENV") == "TEST":
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app.config.from_object(app_config)

db.init_app(app)
with app.app_context():
    db.create_all()

api.add_resource(Event, "/api/events")
api.add_resource(EventDetail, "/api/events/<int:event_id>")
api.add_resource(SignUp, "/api/auth/signup")
api.add_resource(LogIn, "/api/auth/login")
api.add_resource(UserDetail, "/api/profile")