import json
from pathlib import Path

DATA_PATH = Path("data/sample_shells.json")

def load_shells():
    with open(DATA_PATH) as f:
        return json.load(f)

def find_shell(altitude_km: float):
    shells = load_shells()
    for shell in shells:
        if shell["altitude_min"] <= altitude_km <= shell["altitude_max"]:
            return shell
    return None
