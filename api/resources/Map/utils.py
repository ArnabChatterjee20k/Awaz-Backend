from fastapi import WebSocket 
from pydantic import ValidationError
from .schema import MapCoordinates
# from asyncio import async

async def serialise(data:MapCoordinates,ws:WebSocket):
    try:
        return MapCoordinates(**data)
    except Exception as error:
        error:ValidationError
        await ws.send_text(error.json())
        await ws.close()