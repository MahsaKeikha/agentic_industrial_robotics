class SystemArchitectAgent:
    name = "system_architect"
    def run(self, context):
        return {"agent": self.name, "focus": "robotic cell architecture", "inputs": context, "outputs": ["functional decomposition", "interfaces", "assumptions"]}
