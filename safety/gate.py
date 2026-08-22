BLOCKED_ACTIONS = {
    "physical_actuation",
    "plc_write",
    "robot_command",
    "safety_override",
    "disable_interlock",
    "bypass_guard",
    "change_safety_parameters",
    "autonomous_commissioning",
}

REQUIRED_RELEASE_REVIEWS = (
    "hazard_review_complete",
    "simulation_verified",
    "safety_functions_verified",
    "safe_state_verified",
    "interface_review_complete",
    "cybersecurity_review_complete",
    "commissioning_review_complete",
    "human_approval",
)


def authorize(action, approved=False):
    """Authorize non-physical reference actions only.

    Physical execution, safety bypasses, PLC writes, robot commands, and
    commissioning authority remain outside this reference system's scope.
    """
    if action in BLOCKED_ACTIONS:
        return {
            "allowed": False,
            "reason": "consequential physical execution is outside reference system scope",
        }
    return {
        "allowed": bool(approved),
        "reason": "human approval required" if not approved else "approved",
    }


def release_gate(context):
    """Fail closed before any recommendation can be treated as deployment-ready."""
    reasons = []

    for field in REQUIRED_RELEASE_REVIEWS:
        if not context.get(field, False):
            reasons.append(f"missing:{field}")

    if context.get("unresolved_high_risk_hazard", False):
        reasons.append("unresolved_high_risk_hazard")
    if context.get("safety_function_failed", False):
        reasons.append("safety_function_failed")
    if context.get("unsafe_human_robot_separation", False):
        reasons.append("unsafe_human_robot_separation")
    if context.get("unvalidated_motion_plan", False):
        reasons.append("unvalidated_motion_plan")
    if context.get("perception_uncertainty_high", False):
        reasons.append("perception_uncertainty_high")
    if context.get("request_physical_actuation", False):
        reasons.append("physical_actuation_not_authorized")
    if context.get("request_plc_write", False):
        reasons.append("plc_write_not_authorized")
    if context.get("request_robot_command", False):
        reasons.append("robot_command_not_authorized")
    if context.get("request_safety_override", False):
        reasons.append("safety_override_not_authorized")
    if context.get("request_autonomous_commissioning", False):
        reasons.append("autonomous_commissioning_not_authorized")

    return {
        "allowed": not reasons,
        "requires_human_review": True,
        "reasons": reasons,
        "physical_execution_authority": False,
        "safety_override_authority": False,
        "autonomous_commissioning_authority": False,
    }
