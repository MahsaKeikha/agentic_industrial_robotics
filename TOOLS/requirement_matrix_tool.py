def build_requirement_matrix(requirements):
    return [{"id": f"R{i+1}", "text": r, "status": "unverified"} for i, r in enumerate(requirements)]
