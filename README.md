## API Contract

GET /orbit/risk

Parameters:
- altitude_km (float)
- inclination_deg (float)

Response:
- orbit_shell (string)
- object_density (int)
- congestion_index (float)
- collision_probability (float)
- risk_level (string)
