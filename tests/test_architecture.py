from orchestration.orchestrator import run
from safety.gate import authorize

def test_reference_run_blocks_actuation():
    result = run({"objective": "simulation review"})
    assert result["physical_actuation"] is False

def test_safety_gate_blocks_robot_command():
    assert authorize("robot_command", approved=True)["allowed"] is False
