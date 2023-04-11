from fastapi import WebSocket , APIRouter , WebSocketDisconnect , WebSocketException
from .schema import MapCoordinates
from .utils import serialise
from uuid import uuid4
router = APIRouter()

@router.websocket("/ws/")
async def text(ws:WebSocket):
    await ws.accept()
    await ws.send_json({"id":str(uuid4())}) # sending the identifier
    CONNECTION_ACCEPT = True
    while CONNECTION_ACCEPT:
        try:
            data = await ws.receive_json()
            data = await serialise(data=data,ws=ws)
            await ws.send_json(data.dict())
        except Exception as error:
            CONNECTION_ACCEPT = False