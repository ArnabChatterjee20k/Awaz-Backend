import math
from fastapi import WebSocket
from pydantic import ValidationError
from .schema import MapCoordinates, Coordinates
from api import use_cache
from .Data import MapEvent
from pprint import pprint
# from asyncio import async


async def serialise(data: MapCoordinates, ws: WebSocket) -> MapCoordinates:
    try:
        return MapCoordinates(**data)
    except Exception as error:
        error: ValidationError
        await ws.send_text(error.json())
        await ws.close()


async def get_token(ws: WebSocket):
    headers = ws.headers
    token = headers.get("access-token")
    cache = use_cache()
    if not token:
        await ws.send_json({"error": "No access token found"})
        await ws.close()
    # print(cache.get_all())
    return token


def store_user_in_cache(user_email, metadata):
    cache = use_cache()
    cache.add(user_email, metadata)


def clear_from_cache(user_email):
    cache = use_cache()
    cache.remove(id=user_email)


async def broadcast(ws: WebSocket, payload: MapCoordinates):
    """
        ws is the current client who is sending the event
    """
    # sender is the client in danger
    sender_location = payload.location
    sender_lat = sender_location.lat
    sender_long = sender_location.long


    cache = use_cache()

    for connection_id in cache.get_all():
        connection_data = cache.get(connection_id)  # pulling out the data
        """
            example connection_data
            {
                'map_data': {
                        'client': <starlette.websockets.WebSocket object at <>,
                        'data': MapCoordinates(event='DANGER', location=Coordinates(long=11.0, lat=12.0))
                        }
            }
        """
        
        map_data:dict = connection_data.get("map_data")
        if map_data:
            """map_data is None if no client other than the ws is connected to the service"""
            client:WebSocket = map_data.get("client") 

            client_data:MapCoordinates = map_data.get("data")
            
            client_location:Coordinates = client_data.location
            client_lat = client_location.lat
            client_long = client_location.long

            dist_bw_sender_client = distance_between_points(lat1=sender_lat,lon1=sender_long,lat2=client_lat,lon2=client_long)
            is_less_than_max_dist = dist_bw_sender_client<=MapEvent.max_dist
            if ws!=client and is_less_than_max_dist:
                await client.send_json(data=payload.dict())


async def handle_danger(ws: WebSocket, coordinates: Coordinates):
    payload = MapCoordinates(event=MapEvent.danger, location=coordinates)
    await broadcast(ws, payload)


def handle_location(ws: WebSocket, coordinates: Coordinates):
    payload = MapCoordinates(event=MapEvent.location, location=coordinates)
    broadcast(ws, payload)


def distance_between_points(lat1: int | float, lon1: int | float, lat2: int | float, lon2: int | float):
    # convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    r = 6371  # radius of earth in kilometers
    KM_TO_M = 1000
    distance = r * c * KM_TO_M  # multiply by 1000 to get distance in meters

    return distance
