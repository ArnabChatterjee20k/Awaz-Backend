from fastapi import WebSocket , APIRouter , WebSocketDisconnect
from fastapi.logger import logger
from .utils import serialise , get_token , store_user_in_cache , broadcast , clear_from_cache
from .Data import MapEvent
from api.utils.Token import decode_access_token
from api.utils.get_error_info import get_error_info
from api import use_cache

router = APIRouter()

@router.websocket("/ws/")
async def text(ws:WebSocket):
    print("Acceptng")
    await ws.accept()
    token = await get_token(ws)
    email = decode_access_token(token=token).get("email")
    CONNECTION_ACCEPT = True
    cache = use_cache()
    
    store_user_in_cache(user_email=email,metadata={}) # registering the user in the cache so that they can be targeted event further data is not sent

    # this loop will be maintained for every client individually
    while CONNECTION_ACCEPT:
        try:
            data = await ws.receive_json()
            data = await serialise(data=data,ws=ws)
            metadata = {"client":ws,"data":data}
            store_user_in_cache(user_email=email,metadata={"sdf":"dfdf"})
            
            event = data.event
            # if event == MapEvent.danger:
            #     broadcast(ws)
    
        except WebSocketDisconnect:
            # to remove the memory leaks
            CONNECTION_ACCEPT = False
            get_error_info()

        except Exception as error:
            # to remove the memory leaks
            get_error_info()
            CONNECTION_ACCEPT = False
    
    clear_from_cache(user_email=email)