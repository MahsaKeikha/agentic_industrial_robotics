class PerceptionIntegrationAgent:
    name = "perception_integration"
    def run(self, context):
        return {"agent": self.name, "focus": "sensor and perception integration", "inputs": context, "outputs": ["sensor interfaces", "coverage gaps", "data quality checks"]}
