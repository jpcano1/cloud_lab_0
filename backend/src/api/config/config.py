import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "images"

class ProductionConfig(Config):
    POSTGRES_USERNAME = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_DB = os.getenv("POSTGRES_DB")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"

    MAIL_DEFAULT_SENDER = os.getenv("EMAIL_SENDER")
    MAIL_SERVER = os.getenv("EMAIL_SERVER")
    MAIL_PORT = os.getenv("EMAIL_PORT")
    MAIL_USERNAME = os.getenv("EMAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    MAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
    MAIL_USE_SSL = os.getenv("EMAIL_USE_SSL")
    MAIL_DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath("example.db")
    SECRET_KEY = os.getenv("SECRET_KEY", None)
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT", None)
    PORT = 3000
    HOST = "localhost"

    MAIL_DEFAULT_SENDER = os.getenv("EMAIL_SENDER")
    MAIL_SERVER = os.getenv("EMAIL_SERVER")
    MAIL_PORT = os.getenv("EMAIL_PORT")
    MAIL_USERNAME = os.getenv("EMAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    MAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
    MAIL_USE_SSL = os.getenv("EMAIL_USE_SSL")

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "<Testing DB URL>"
    SQLALCHEMY_ECHO = False