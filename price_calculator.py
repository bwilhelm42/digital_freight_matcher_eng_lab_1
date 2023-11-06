MARKUP = 0.5
PALLET_COST_PER_MILE = 0.0683053788345865
PACKAGE_COST_PER_MILE = 0.0192470664936441

def calculate(miles: int, packages: int = 0, pallets: int = 0) -> float:
    pallet_cost = pallets * PALLET_COST_PER_MILE * miles
    package_cost = packages * PACKAGE_COST_PER_MILE * miles
    return (package_cost + pallet_cost) * (1 + MARKUP)