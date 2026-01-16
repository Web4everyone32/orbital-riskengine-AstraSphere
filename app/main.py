from fastapi import FastAPI
from app.routes.ui import router as ui_router
from app.routes.map import router as map_router
from app.routes.map import router as map_router
from app.routes.satellites import router as satellite_router
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.orbit import router as orbit_router
from app.routes.map import router as map_router
from app.routes.satellites import router as satellites_router


app = FastAPI(
    title="Orbital Risk Engine",
    description="""
### Module A — Space Debris & Orbital Congestion Intelligence

This service statistically models Low Earth Orbit (LEO) shells and computes
congestion and collision risk scores.

**Purpose**
- Strategic orbital risk intelligence
- Planning and sustainability analysis
- Downstream Earth-observation impact modeling

⚠️ This system does **not** perform real-time tracking or satellite control.
""",
    version="0.1.0",
    contact={
        "name": "Orbital Sustainability Intelligence",
        "url": "https://github.com/<your-username>/orbital-risk-engine"
    },
    license_info={"name": "MIT"}
)

app = FastAPI(
    title="AstraSphere – Orbital Intelligence Platform",
    description="Visual orbital intelligence and congestion risk analysis",
    version="1.0.0"
)

app.include_router(orbit_router)
app.include_router(map_router)
app.include_router(satellites_router)
app.include_router(ui_router)
app.include_router(map_router, tags=["Space Map"])
app.include_router(map_router, tags=["Space Map"])
app.include_router(satellite_router, tags=["Satellites"])
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/static", StaticFiles(directory="static"), name="static")

