from pydantic import BaseModel

class RiskMetrics(BaseModel):
    object_density: int
    congestion_index: float
    collision_probability: float

class RiskInfo(BaseModel):
    level: str
    color: str

class OrbitRiskResponse(BaseModel):
    orbit_shell: str
    metrics: RiskMetrics
    risk: RiskInfo
