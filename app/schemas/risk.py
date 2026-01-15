from pydantic import BaseModel

class OrbitRiskResponse(BaseModel):
    orbit_shell: str
    object_density: int
    congestion_index: float
    collision_probability: float
    risk_level: str
