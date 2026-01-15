from fastapi import APIRouter, HTTPException, Query
from app.schemas.risk import OrbitRiskResponse
from app.services.shell_model import find_shell
from app.services.congestion_model import calculate_congestion_index
from app.services.risk_model import classify_risk, estimate_collision_probability

router = APIRouter()

@router.get(
    "/orbit/risk",
    response_model=OrbitRiskResponse,
    summary="Compute orbital congestion and collision risk",
    description="Returns congestion index and collision risk for a given orbital altitude and inclination."
)
def get_orbit_risk(
    altitude_km: float = Query(
        ...,
        example=550,
        description="Orbital altitude in kilometers"
    ),
    inclination_deg: float = Query(
        ...,
        example=97,
        description="Orbital inclination in degrees"
    )
):
    shell = find_shell(altitude_km)

    if not shell:
        raise HTTPException(status_code=404, detail="No orbital shell found")

    congestion_index = calculate_congestion_index(
        shell["base_density"],
        shell["inclination_factor"]
    )

    risk_level = classify_risk(congestion_index)

    color_map = {
        "LOW": "green",
        "MEDIUM": "orange",
        "HIGH": "red",
        "CRITICAL": "darkred"
    }

    return OrbitRiskResponse(
        orbit_shell=shell["shell"],
        metrics={
            "object_density": shell["base_density"],
            "congestion_index": congestion_index,
            "collision_probability": estimate_collision_probability(congestion_index)
        },
        risk={
            "level": risk_level,
            "color": color_map[risk_level]
        }
    )
