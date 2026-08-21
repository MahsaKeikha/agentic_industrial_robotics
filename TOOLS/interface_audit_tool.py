def audit_interfaces(interfaces):
    return {"interfaces": interfaces, "checks": ["ownership", "protocol", "failure behavior", "fallback"]}
