# Living Bridge OS v0.1

**A continuity-first multi-agent operating environment.**

Conversations become persistent knowledge, artifacts, memory, and evolving collaboration.

## Quick Start

```bash
pip install -r requirements.txt

# Start API
uvicorn bridge.api.server:app --reload

# Start Dashboard
streamlit run bridge/ui/dashboard.py
```

## Status
Multi-agent orchestration with simulated agents (no external APIs yet). Full spec being implemented step by step.
