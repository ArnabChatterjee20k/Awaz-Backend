from dotenv import load_dotenv
from os import environ
load_dotenv(".env")

class Config:
    SECRET_KEY = environ.get("SECRET_KEY")
    ALGORITHM = environ.get("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")