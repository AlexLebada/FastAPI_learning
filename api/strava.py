import fastapi
from models.strava import KilometersRequest
from controllers.strava import assess_target

# .APIRouter() class create modular routes
router = fastapi.APIRouter()

@router.post("/calculate_strava")
def calculate_strava(km_request: KilometersRequest):
    target = km_request.target
    kms = km_request.kilometers

    message = assess_target(kms, target)
    return {"message": message}