from fastapi import APIRouter
import time
import math

router = APIRouter()

@router.get("/api/satellites")
def get_satellites():
    t = time.time()

    return [
        {
            "id": "ASTRA-LEO-01",
            "name": "AstraSphere DemoSat 1",
            "altitude_km": 550,
            "inclination_deg": 97,
            "lat": math.sin(t / 30) * 30,
            "lon": (t * 2) % 360 - 180
        },
        {
            "id": "ASTRA-LEO-02",
            "name": "AstraSphere DemoSat 2",
            "altitude_km": 600,
            "inclination_deg": 98,
            "lat": math.cos(t / 40) * 45,
            "lon": (t * 1.5) % 360 - 180
        }
    ]
