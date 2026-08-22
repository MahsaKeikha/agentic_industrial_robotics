from orchestration.orchestrator import run


context = {
    "objective": "review a simulated robotic cell redesign",
    "constraints": ["simulation only"],
    "hazard_review_complete": True,
    "simulation_verified": True,
    "safety_functions_verified": True,
    "safe_state_verified": True,
    "interface_review_complete": True,
    "cybersecurity_review_complete": True,
    "commissioning_review_complete": True,
    "human_approval": True,
}

print(run(context))
