from orchestration.orchestrator import run


def approved_reference_context():
    return {
        "objective": "industrial robotics engineering review",
        "hazard_review_complete": True,
        "simulation_verified": True,
        "safety_functions_verified": True,
        "safe_state_verified": True,
        "interface_review_complete": True,
        "cybersecurity_review_complete": True,
        "commissioning_review_complete": True,
        "human_approval": True,
    }


if __name__ == "__main__":
    print(run(approved_reference_context()))
