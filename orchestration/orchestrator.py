from AGENTS.system_architect_agent import SystemArchitectAgent
from AGENTS.motion_planning_agent import MotionPlanningAgent
from AGENTS.perception_integration_agent import PerceptionIntegrationAgent
from AGENTS.safety_validation_agent import SafetyValidationAgent
from AGENTS.commissioning_agent import CommissioningAgent
from AGENTS.lifecycle_reliability_agent import LifecycleReliabilityAgent
from safety.gate import release_gate

AGENTS = [
    SystemArchitectAgent(),
    MotionPlanningAgent(),
    PerceptionIntegrationAgent(),
    SafetyValidationAgent(),
    CommissioningAgent(),
    LifecycleReliabilityAgent(),
]


def run(context):
    results = [agent.run(context) for agent in AGENTS]
    governance = release_gate(context)
    return {
        "system": "F71",
        "results": results,
        "governance": governance,
        "status": "approved_for_reference_use" if governance["allowed"] else "blocked_pending_review",
        "physical_actuation": False,
        "physical_execution_authority": False,
    }
