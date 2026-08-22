from orchestration.orchestrator import run
from safety.gate import authorize, release_gate


def approved_context():
    return {
        "objective": "simulation review",
        "hazard_review_complete": True,
        "simulation_verified": True,
        "safety_functions_verified": True,
        "safe_state_verified": True,
        "interface_review_complete": True,
        "cybersecurity_review_complete": True,
        "commissioning_review_complete": True,
        "human_approval": True,
    }


def test_reference_run_blocks_actuation():
    result = run(approved_context())
    assert result["physical_actuation"] is False
    assert result["physical_execution_authority"] is False


def test_complete_reference_case_can_pass_governance():
    assert release_gate(approved_context())["allowed"] is True


def test_missing_hazard_review_fails_closed():
    context = approved_context()
    context["hazard_review_complete"] = False
    assert release_gate(context)["allowed"] is False


def test_high_risk_hazard_blocks_release():
    context = approved_context()
    context["unresolved_high_risk_hazard"] = True
    assert release_gate(context)["allowed"] is False


def test_safety_function_failure_blocks_release():
    context = approved_context()
    context["safety_function_failed"] = True
    assert release_gate(context)["allowed"] is False


def test_robot_command_is_never_authorized():
    assert authorize("robot_command", approved=True)["allowed"] is False


def test_safety_override_is_never_authorized():
    assert authorize("safety_override", approved=True)["allowed"] is False


def test_autonomous_commissioning_is_never_authorized():
    assert authorize("autonomous_commissioning", approved=True)["allowed"] is False
