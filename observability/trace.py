def trace_event(agent, event, payload=None):
    return {"agent": agent, "event": event, "payload": payload or {}}
