from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bridge.core.orchestrator import Orchestrator
from bridge.core.mission import Mission

app = FastAPI(title="Living Bridge OS")

orchestrator = Orchestrator()

@app.post("/mission")
async def create_mission(mission: Mission):
    result = orchestrator.execute_mission(mission.dict())
    return result.dict()

@app.get("/")
def root():
    return {"status": "Living Bridge OS v0.1 running"}