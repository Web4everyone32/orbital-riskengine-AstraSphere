from fastapi import APIRouter, HTTPException
from app.schemas.risk import OrbitRiskResponse
from app.services.shell_model import find_shell
from app.services.congestion_model import calculate_congestion_index
from app.services.risk_model import classify_risk, estimate_collision_probability

router = APIRouter()

@router.get("/orbit/risk", response_model=OrbitRiskResponse)
def get_orbit_risk(altitude_km: float, inclination_deg: float):
    shell = find_shell(altitude_km)

    if not shell:
        raise HTTPException(status_code=404, detail="No orbital shell found")

    congestion_index = calculate_congestion_index(
        shell["base_density"],
        shell["inclination_factor"]
    )

    return OrbitRiskResponse(
        orbit_shell=shell["shell"],
        object_density=shell["base_density"],
        congestion_index=congestion_index,
        collision_probability=estimate_collision_probability(congestion_index),
        risk_level=classify_risk(congestion_index)
    )
