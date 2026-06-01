from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from ..core.mission import Mission
from ..core.orchestrator import Orchestrator
from ..core.registry import AgentRegistry
import uvicorn

app = FastAPI(title="Living Bridge OS API", version="0.1")

# TODO: Initialize registry and orchestrator with real agents
registry = AgentRegistry()
orchestrator = registry.get_orchestrator()

class MissionRequest(BaseModel):
    objective: str
    constraints: List[str] = []
    agents: List[str] = ["architect", "explorer", "verifier"]

@app.post("/mission")
async def create_mission(request: MissionRequest):
    """Create and execute a new mission."""
    mission = Mission(
        objective=request.objective,
        constraints=request.constraints,
        agents=request.agents
    )
    result = await orchestrator.execute_mission(mission)
    return {"mission": mission.model_dump(), "result": result}

@app.get("/mission/{mission_id}")
async def get_mission(mission_id: str):
    """Get mission details (stub)."""
    return {"mission_id": mission_id, "status": "todo - implement persistence"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
