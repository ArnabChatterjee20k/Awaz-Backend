from .Token import decode_access_token
from fastapi import Header , HTTPException

def token_required(token:str|None=Header()):
    try:
        return decode_access_token(token)
    except:
        raise HTTPException(status_code=403,detail="No token found")