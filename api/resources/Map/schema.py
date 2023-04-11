from pydantic import BaseModel

class Coordinates(BaseModel):
    long:float|int
    lat:float|int

class MapCoordinates(BaseModel):
    event:str
    location:Coordinates