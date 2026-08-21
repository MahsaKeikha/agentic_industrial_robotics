from AGENTS.system_architect_agent import SystemArchitectAgent
from AGENTS.motion_planning_agent import MotionPlanningAgent
from AGENTS.perception_integration_agent import PerceptionIntegrationAgent
from AGENTS.safety_validation_agent import SafetyValidationAgent
from AGENTS.commissioning_agent import CommissioningAgent
from AGENTS.lifecycle_reliability_agent import LifecycleReliabilityAgent

AGENTS = [SystemArchitectAgent(), MotionPlanningAgent(), PerceptionIntegrationAgent(), SafetyValidationAgent(), CommissioningAgent(), LifecycleReliabilityAgent()]

def run(context):
    return {"system": "F71", "results": [agent.run(context) for agent in AGENTS], "physical_actuation": False}
