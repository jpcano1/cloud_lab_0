from flask import Flask
from .api.utils import db
from dotenv import load_dotenv, find_dotenv
from .api.config import (
    DevelopmentConfig,
    ProductionConfig,
    TestingConfig
)
import os, sys
import logging

logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s|%(levelname)s|%(filename)s: %(lineno)s| %(message)s",
    level=logging.DEBUG
)

load_dotenv(find_dotenv())

app = Flask(__name__)

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