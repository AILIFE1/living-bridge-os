# Living Bridge OS v0.1

A continuity-first multi-agent operating environment where conversations become persistent knowledge, artifacts, memory, and evolving collaboration.

## Core Philosophy
Question → Discussion → Artifact → Memory → Future Context

## Quick Start
```bash
pip install -r requirements.txt
uvicorn bridge.api.server:app --reload
streamlit run bridge/ui/dashboard.py
```

See `docs/architecture.md` for details.

## Status
v0.1 - Core orchestrator, agents, memory, SQLite persistence, API, and dashboard implemented.