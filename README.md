# Living Bridge OS v0.1

**A continuity-first multi-agent AI operating environment**

Conversations → Discussion → Artifact → Memory → Future Context

The system orchestrates Claude (Architect), Grok (Explorer), OpenAI (Verifier), Gemini (Analyst) in a persistent, collaborative workspace.

## Installation
```bash
git clone https://github.com/AILIFE1/living-bridge-os.git
cd living-bridge-os
pip install -r requirements.txt
```

## Running
- API: `uvicorn bridge.api.server:app --reload`
- Dashboard: `streamlit run bridge/ui/dashboard.py`

Full implementation following the Master Build Specification. Core modules are in place.

See `docs/architecture.md` for details.

**Status**: Building incrementally - v0.1 core in progress.