from dotenv import load_dotenv
from os import environ
load_dotenv(".env")

class Config:
    SECRET_KEY = environ.get("SECRET_KEY")
    ALGORITHM = environ.get("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
    SQLALCHEMY_DATABASE_URL = environ.get("SQLALCHEMY_DATABASE_URL")

    VONAGE_KEY = environ.get("VONAGE_KEY")
    VONAGE_SECRET = environ.get("VONAGE_SECRET")

    PRODUCTION = environ.get("PRODUCTION") == "PRODUCTION"