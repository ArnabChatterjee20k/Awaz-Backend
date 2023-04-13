from fastapi import APIRouter,Depends
from .schema import UserCreate , UserLogin
from .utils import create_new_user , verify_user
from ...db.db import get_db
from sqlalchemy.orm import Session
from api.utils.Token import create_access_token

router = APIRouter()

@router.post("/")
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    new_user = create_new_user(db,user)
    token = create_access_token({"email":new_user.email,"id":new_user.id})
    return dict(**new_user.dict(),**{"access-token":token})

# @router.get("/{user_id}")
# def get_user(user_id:int,db:Session=Depends(get_db),token:str=Depends(token_required)):
#     user = get_user_by_id(db,user_id)
#     new_user = UserResult.from_orm(user)
#     return new_user

@router.post("/login")
def login_user(user:UserLogin=None,db:Session=Depends(get_db)):
    user = verify_user(db,user.email,user.password)
    token = create_access_token({"email":user.email,"id":user.id})
    return dict(**user.dict(),**{"access-token":token})

    