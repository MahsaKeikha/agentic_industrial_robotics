class MotionPlanningAgent:
    name = "motion_planning"
    def run(self, context):
        return {"agent": self.name, "focus": "simulation only motion planning review", "inputs": context, "outputs": ["workspace constraints", "trajectory risks", "simulation checks"]}
