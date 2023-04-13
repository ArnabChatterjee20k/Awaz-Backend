from fastapi import WebSocket 
from pydantic import ValidationError
from .schema import MapCoordinates , Coordinates
from api import use_cache
from .Data import MapEvent
from pprint import pprint
# from asyncio import async

async def serialise(data:MapCoordinates,ws:WebSocket):
    try:
        return MapCoordinates(**data)
    except Exception as error:
        error:ValidationError
        await ws.send_text(error.json())
        await ws.close()

async def get_token(ws:WebSocket):
    headers = ws.headers
    token = headers.get("access-token")
    cache = use_cache()
    if not token:
        await ws.send_json({"error":"No access token found"})
        await ws.close()
    # print(cache.get_all())
    return token

def store_user_in_cache(user_email,metadata):
    cache = use_cache()
    cache.add(user_email,metadata)

def clear_from_cache(user_email):
    cache = use_cache()
    cache.remove(id=user_email)

def broadcast(ws:WebSocket,payload:MapCoordinates):
    cache = use_cache()
    for connections in cache.get_all():
        client:WebSocket = connections.get("client")
        if client!=ws:
            ws.send_text("danger")

def handle_danger(ws:WebSocket,coordinates:Coordinates):
    payload = MapCoordinates(event=MapEvent.danger,location=coordinates)
    broadcast(ws,payload)

import math

def distance_between_points(lat1:int|float, lon1:int|float, lat2:int|float, lon2:int|float):
    # convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    r = 6371 # radius of earth in kilometers
    KM_TO_M = 1000
    distance = r * c * KM_TO_M # multiply by 1000 to get distance in meters

    return distance
