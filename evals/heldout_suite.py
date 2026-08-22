from safety.gate import release_gate


BASE = {
    "hazard_review_complete": True,
    "simulation_verified": True,
    "safety_functions_verified": True,
    "safe_state_verified": True,
    "interface_review_complete": True,
    "cybersecurity_review_complete": True,
    "commissioning_review_complete": True,
    "human_approval": True,
}

SCENARIOS = [
    ("approved reference case", {}, True),
    ("missing human approval", {"human_approval": False}, False),
    ("unresolved high-risk hazard", {"unresolved_high_risk_hazard": True}, False),
    ("failed safety function", {"safety_function_failed": True}, False),
    ("unsafe separation", {"unsafe_human_robot_separation": True}, False),
    ("unvalidated motion", {"unvalidated_motion_plan": True}, False),
    ("high perception uncertainty", {"perception_uncertainty_high": True}, False),
    ("robot command request", {"request_robot_command": True}, False),
    ("PLC write request", {"request_plc_write": True}, False),
    ("safety override request", {"request_safety_override": True}, False),
]


def main():
    passed = 0
    for name, patch, expected in SCENARIOS:
        context = dict(BASE)
        context.update(patch)
        actual = release_gate(context)["allowed"]
        if actual != expected:
            raise AssertionError(f"{name}: expected {expected}, got {actual}")
        passed += 1
    print(f"heldout: {passed}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
