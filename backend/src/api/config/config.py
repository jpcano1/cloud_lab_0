import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config(object):
    POSTGRES_USERNAME = os.getenv("POSTGRES_USER", None)
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", None)
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", None)
    POSTGRES_DB = os.getenv("POSTGRES_DB", None)

    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "images"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "<Production DB URL>"

    MAIL_DEFAULT_SENDER = os.getenv("EMAIL_SENDER")
    MAIL_SERVER = os.getenv("EMAIL_SERVER")
    MAIL_PORT = os.getenv("EMAIL_PORT")
    MAIL_USERNAME = os.getenv("EMAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    MAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
    MAIL_USE_SSL = os.getenv("EMAIL_USE_SSL")
    MAIL_DEBUG = False

    UPLOAD_FOLDER = None

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{Config.POSTGRES_USERNAME}:{Config.POSTGRES_PASSWORD}@{Config.POSTGRES_HOST}:5432/{Config.POSTGRES_DB}"
    SECRET_KEY = os.getenv("SECRET_KEY", None)
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT", None)

    # Localhost configurations
    # MAIL_DEFAULT_SENDER = "test@email.com"
    # MAIL_SERVER = "localhost"
    # MAIL_PORT = 1025
    # MAIL_USERNAME = None
    # MAIL_PASSWORD = None
    # MAIL_USE_TLS = True
    # MAIL_USE_SSL = False
    # MAIL_SUPPRESS_SEND = True
    # MAIL_DEBUG = True

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