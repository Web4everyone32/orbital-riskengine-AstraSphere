from fastapi import FastAPI
from app.routes.ui import router as ui_router
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

app.include_router(ui_router)
