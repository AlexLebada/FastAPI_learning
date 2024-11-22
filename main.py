# import FastAPI class
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import strava
from views import strava_target

app = FastAPI()

# maps a new route to the specified path for static files
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(strava.router_1)
app.include_router(strava_target.router_2)


