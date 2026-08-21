# F71 Agentic Industrial Robotics

A standalone multi-agent AI reference implementation for industrial robotics engineering, simulation, safety analysis, commissioning planning, and lifecycle governance.

## Architecture

### Agents
- [System Architect Agent](AGENTS/system_architect_agent.py)
- [Motion Planning Agent](AGENTS/motion_planning_agent.py)
- [Perception Integration Agent](AGENTS/perception_integration_agent.py)
- [Safety Validation Agent](AGENTS/safety_validation_agent.py)
- [Commissioning Agent](AGENTS/commissioning_agent.py)
- [Lifecycle Reliability Agent](AGENTS/lifecycle_reliability_agent.py)

### Tools
- [Requirement Matrix Tool](TOOLS/requirement_matrix_tool.py)
- [Simulation Tool](TOOLS/simulation_tool.py)
- [Hazard Register Tool](TOOLS/hazard_register_tool.py)
- [Interface Audit Tool](TOOLS/interface_audit_tool.py)
- [Traceability Tool](TOOLS/traceability_tool.py)

### Skills
- [Robotic Cell Architecture](SKILLS/robotic_cell_architecture.py)
- [Motion Planning Review](SKILLS/motion_planning_review.py)
- [Safety Case Development](SKILLS/safety_case_development.py)
- [Commissioning Readiness](SKILLS/commissioning_readiness.py)
- [Reliability Analysis](SKILLS/reliability_analysis.py)

## Supporting layers

`orchestration/`, `memory/`, `state/`, `schemas/`, `prompts/`, `config/`, `safety/`, `observability/`, `evals/`, `benchmarks/`, `examples/`, `tests/`, and `docs/` provide the full reference architecture.

## Safety boundary

This project supports engineering analysis, simulation, documentation, and review. It does not autonomously issue commands to physical robots, PLCs, actuators, or industrial equipment. Any physical deployment requires qualified engineering review, site specific risk assessment, and authorized human control.

## Run

```bash
python run.py
python -m pytest -q
```
