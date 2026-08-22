# Agentic Industrial Robotics

**F71 | L3 Gold Standard | v1.0**

A governed six-agent reference system for industrial robotics engineering, simulation, safety analysis, commissioning planning, and lifecycle reliability.

## Core agents

- [System Architect Agent](AGENTS/system_architect_agent.py)
- [Motion Planning Agent](AGENTS/motion_planning_agent.py)
- [Perception Integration Agent](AGENTS/perception_integration_agent.py)
- [Safety Validation Agent](AGENTS/safety_validation_agent.py)
- [Commissioning Agent](AGENTS/commissioning_agent.py)
- [Lifecycle Reliability Agent](AGENTS/lifecycle_reliability_agent.py)

## Gold-standard governance

F71 is a reference and review system, not a physical robot controller. The release gate fails closed unless hazard review, simulation verification, safety-function verification, safe-state verification, interface review, cybersecurity review, commissioning review, and qualified human approval are complete.

It also blocks unresolved high-risk hazards, failed safety functions, unsafe human-robot separation, unvalidated motion plans, high perception uncertainty, direct robot commands, PLC writes, physical actuation, safety overrides, interlock bypasses, and autonomous commissioning.

Physical execution authority: **false**  
Safety override authority: **false**  
Autonomous commissioning authority: **false**

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and executes:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/heldout_suite.py
python examples/example.py
python run.py
```

The behavioral suite includes direct fail-closed tests plus a 10-scenario held-out governance suite.

## Architecture

[`AGENTS/`](AGENTS/) | [`TOOLS/`](TOOLS/) | [`SKILLS/`](SKILLS/) | [`orchestration/`](orchestration/) | [`memory/`](memory/) | [`state/`](state/) | [`schemas/`](schemas/) | [`prompts/`](prompts/) | [`config/`](config/) | [`safety/`](safety/) | [`observability/`](observability/) | [`evals/`](evals/) | [`benchmarks/`](benchmarks/) | [`examples/`](examples/) | [`tests/`](tests/) | [`docs/`](docs/)

## Safety boundary

The system may support engineering analysis, simulation, documentation, and review. It must not autonomously issue commands to physical robots, PLCs, actuators, safety systems, or industrial equipment. Any real deployment requires site-specific risk assessment, verified safety functions, qualified engineering review, and authorized human control.

## Run

```bash
python run.py
python -m pytest -q
python evals/heldout_suite.py
```
