def hazard_register(hazards):
    return [{"hazard": h, "status": "requires_review", "owner": "qualified_human"} for h in hazards]
