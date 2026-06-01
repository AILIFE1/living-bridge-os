# Living Bridge OS v0.1

**Continuity-first multi-agent AI operating environment**

Conversations become persistent knowledge, artifacts, memory, and evolving collaboration.

The system is an operating environment for human-mediated collaboration between multiple AI systems (Claude, Grok, OpenAI, Gemini).

## Quick Start

```bash
pip install -r requirements.txt
uvicorn bridge.api.server:app --reload
streamlit run bridge/ui/dashboard.py
```

Full implementation in progress based on the Master Build Specification.