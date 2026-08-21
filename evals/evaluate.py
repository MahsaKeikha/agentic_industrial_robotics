def evaluate(result):
    required = ["system", "results", "physical_actuation"]
    return {"passed": all(k in result for k in required) and result.get("physical_actuation") is False}
