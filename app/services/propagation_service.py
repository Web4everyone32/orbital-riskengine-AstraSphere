from skyfield.api import EarthSatellite, load
from datetime import datetime, timedelta
from app.services.tle_store import TLE_DATA

ts = load.timescale()

def propagate_at_time(name: str, time: datetime):
    tle = TLE_DATA.get(name)
    if not tle:
        return None

    sat = EarthSatellite(tle[0], tle[1], name, ts)
    t = ts.from_datetime(time)
    geo = sat.at(t)
    sub = geo.subpoint()

    return {
        "name": name,
        "lat": sub.latitude.degrees,
        "lon": sub.longitude.degrees,
        "altitude_km": sub.elevation.km
    }

def generate_ground_track(name: str, minutes=90, step=2):
    now = datetime.utcnow()
    track = []

    for i in range(-minutes, minutes, step):
        pos = propagate_at_time(name, now + timedelta(minutes=i))
        if pos:
            track.append({
                "lat": pos["lat"],
                "lon": pos["lon"]
            })

    return track
