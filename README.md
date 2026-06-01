# Living Bridge OS v0.1

**A continuity-first multi-agent operating environment.**

Conversations become persistent knowledge, artifacts, memory, and evolving collaboration.

## Core Philosophy
Question → Discussion → Artifact → Memory → Future Context

The system is an operating environment for human-mediated collaboration between multiple AI agents (Claude Architect, Grok Explorer, OpenAI Verifier, Gemini Analyst).

## Current Status (v0.1)
- ✅ Full repository structure
- ✅ Pydantic models (Mission, AgentResponse)
- ✅ Agent system with simulated responses (no real APIs yet, as requested)
- ✅ AgentRegistry with all 4 agents
- ✅ Orchestrator with mission execution, agent dispatch, debate, synthesis, and memory integration
- ✅ SQLite persistence foundation
- ✅ FastAPI API (`/mission` endpoint)
- ✅ Streamlit dashboard
- ✅ Core memory layers (working memory implemented)

## Quick Start
```bash
git clone https://github.com/AILIFE1/living-bridge-os.git
cd living-bridge-os
pip install -r requirements.txt

# Terminal 1: API
uvicorn bridge.api.server:app --reload

# Terminal 2: Dashboard
streamlit run bridge/ui/dashboard.py
```

Send a mission via the API or dashboard and watch the multi-agent collaboration unfold!

## Next
- Full Debate + Synthesis engines polish
- Artifact Store
- Enhanced memory (episodic, codex)
- Dashboard improvements

Built exactly per the Master Build Specification.
