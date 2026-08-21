def authorize(action, approved=False):
    blocked = {"physical_actuation", "plc_write", "robot_command", "safety_override"}
    if action in blocked:
        return {"allowed": False, "reason": "physical execution is outside reference system scope"}
    return {"allowed": bool(approved), "reason": "human approval required" if not approved else "approved"}
