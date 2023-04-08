from pydantic import BaseModel, EmailStr, constr, FileUrl
from api.utils import Regex

password_regex = Regex.password_regex()
phone_number_regex = Regex.phone_number_regex()


class UserBase(BaseModel):
    """The base class which provides the details"""
    name: str
    email: EmailStr
    phone_number: constr(regex=phone_number_regex, strip_whitespace=True)
    voice: FileUrl = None

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: constr(regex=password_regex, strip_whitespace=True)

class UserResult(BaseModel):
    id: int
    name: str
    email: EmailStr
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email:EmailStr
    password:str