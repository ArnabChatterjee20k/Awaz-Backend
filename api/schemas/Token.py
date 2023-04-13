from pydantic import BaseModel , EmailStr
class Token(BaseModel):
    email:EmailStr
    id:int