from dataclasses import dataclass, field
@dataclass
class RunState:
    status: str = "planned"
    evidence: list = field(default_factory=list)
    approvals: list = field(default_factory=list)
