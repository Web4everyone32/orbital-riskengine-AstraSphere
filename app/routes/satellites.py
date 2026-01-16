from fastapi import APIRouter
from datetime import datetime
from app.services.propagation_service import (
    propagate_at_time,
    generate_ground_track
)
from app.services.conjunction_service import detect_conjunctions
from app.services.tle_store import TLE_DATA

router = APIRouter()
SAT_NAMES = list(TLE_DATA.keys())

@router.get("/api/satellites")
def get_satellites():
    now = datetime.utcnow()
    sats = []

    for name in SAT_NAMES:
        pos = propagate_at_time(name, now)
        if pos:
            pos["id"] = name
            sats.append(pos)

    return sats

@router.get("/api/groundtrack/{sat_name}")
def ground_track(sat_name: str):
    return generate_ground_track(sat_name)

@router.get("/api/conjunctions")
def conjunctions():
    return detect_conjunctions(SAT_NAMES)
