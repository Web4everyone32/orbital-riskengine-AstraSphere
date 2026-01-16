import numpy as np
from datetime import datetime
from app.services.propagation_service import propagate_at_time

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # km
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(np.radians(lat1))
        * np.cos(np.radians(lat2))
        * np.sin(dlon / 2) ** 2
    )
    return 2 * R * np.arcsin(np.sqrt(a))

def detect_conjunctions(sat_names, threshold_km=50):
    now = datetime.utcnow()
    positions = []

    for s in sat_names:
        pos = propagate_at_time(s, now)
        if pos:
            positions.append(pos)

    alerts = []

    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            d = haversine(
                positions[i]["lat"],
                positions[i]["lon"],
                positions[j]["lat"],
                positions[j]["lon"]
            )
            if d < threshold_km:
                alerts.append({
                    "pair": (positions[i]["name"], positions[j]["name"]),
                    "distance_km": round(d, 2),
                    "risk": "HIGH"
                })

    return alerts
