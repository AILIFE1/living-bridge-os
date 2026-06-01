from fastapi import FastAPI
from bridge.core.mission import Mission
from bridge.core.orchestrator import Orchestrator

app = FastAPI(title="Living Bridge OS API")

orchestrator = Orchestrator()

@app.post("/mission")
async def create_mission(mission: Mission):
    result = await orchestrator.process_mission(mission)
    return result

@app.get("/")
def root():
    return {"message": "Living Bridge OS v0.1 API running"}