from fastapi import FastAPI
from app.routes.orbit import router as orbit_router

app = FastAPI(
    title="Orbital Risk Engine",
    description="Module A: Space Debris & Orbital Congestion Intelligence",
    version="0.1.0"
)

app.include_router(orbit_router)
