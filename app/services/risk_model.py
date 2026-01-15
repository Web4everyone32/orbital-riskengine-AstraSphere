def classify_risk(congestion_index: float):
    if congestion_index < 0.3:
        return "LOW"
    elif congestion_index < 0.6:
        return "MEDIUM"
    elif congestion_index < 0.8:
        return "HIGH"
    else:
        return "CRITICAL"

def estimate_collision_probability(congestion_index: float):
    # Order-of-magnitude statistical estimate
    return round(congestion_index * 0.003, 4)
