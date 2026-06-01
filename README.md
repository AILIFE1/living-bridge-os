# Living Bridge OS v0.1

**A continuity-first multi-agent operating environment**

Conversations become persistent knowledge, artifacts, memory, and evolving collaboration.

The system is an operating environment for human-mediated collaboration between multiple AI systems (Claude, Grok, OpenAI, Gemini).

## Core Philosophy
- Traditional AI: Question → Answer → Forget
- Living Bridge OS: Question → Discussion → Artifact → Memory → Future Context

## Features (v0.1)
- Multi-agent orchestration (Architect, Explorer, Verifier, Analyst)
- Debate Engine + Consensus Engine
- Persistent Memory layers (Working, Episodic, Codex)
- Artifact Store
- FastAPI backend
- Streamlit dashboard
- SQLite persistence

## Quick Start
```bash
pip install -r requirements.txt
uvicorn bridge.api.server:app --reload
streamlit run bridge/ui/dashboard.py
```

See `docs/architecture.md` for full details.

Built from the Master Build Specification.