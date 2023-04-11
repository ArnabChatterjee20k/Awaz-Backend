from fastapi import FastAPI
from api.resources.User import User
# from api.resources.Contacts import Contacts
from api.resources.Map import Map
from api.db.db import engine,Base

import uvicorn
api = FastAPI()
Base.metadata.create_all(bind = engine)

api.include_router(User.router,prefix="/user")
# api.include_router(Contacts.router,prefix="/contacts")
api.include_router(Map.router , prefix="/map")

if __name__ == "__main__":
    uvicorn.run("main:api",reload=True)