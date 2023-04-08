from .schema import UserCreate, UserBase, UserResult , UserLogin
from sqlalchemy.orm import Session
from api.models.User import User
from api.utils.Token import verify_password
from fastapi import HTTPException
from pydantic import EmailStr

def verify_user(db: Session, email: EmailStr,password:str):
    user = db.query(User).filter(User.email == email).first()
    received_password = password
    exisiting_password = user.password
    
    if verify_password(received_password,exisiting_password):
        return UserResult.from_orm(user)
    
    raise HTTPException(status_code=403)

def get_user_by_id(db:Session,id:int):
    return db.query(User).filter(User.id == id).first()

def get_user_by_email(db:Session,email:EmailStr):
    return db.query(User).filter(User.email==email).first()

def create_new_user(db: Session, user: UserCreate):
    user_exists = get_user_by_email(db,email=user.email)
    if user_exists:
        raise HTTPException(status_code=400,detail="Email already registered")
    
    new_user_details = UserBase(**user.dict())
    new_user = User(**new_user_details.dict())
    new_user.password = user.password
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return UserResult.from_orm(new_user)