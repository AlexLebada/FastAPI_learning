# import FastAPI class
from fastapi import FastAPI
from api import strava

app = FastAPI()

app.include_router(strava.router)


