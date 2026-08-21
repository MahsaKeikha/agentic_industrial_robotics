class CommissioningAgent:
    name = "commissioning"
    def run(self, context):
        return {"agent": self.name, "focus": "commissioning readiness planning", "inputs": context, "outputs": ["checklist", "hold points", "evidence required"]}
