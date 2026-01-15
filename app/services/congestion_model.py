def calculate_congestion_index(base_density: int, inclination_factor: float):
    # Normalize density against a reference max (configurable later)
    density_score = min(base_density / 2000, 1.0)

    congestion_index = density_score * inclination_factor

    return round(congestion_index, 2)
