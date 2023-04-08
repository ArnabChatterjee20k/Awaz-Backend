from fastapi import FastAPI
from api.resources.User import User
from api.db.db import engine,Base

import uvicorn
api = FastAPI()

api.include_router(User.router,prefix="/user")

if __name__ == "__main__":
    uvicorn.run("main:api",reload=True)