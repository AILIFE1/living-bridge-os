from fastapi import FastAPI
from bridge.core.orchestrator import Orchestrator
from bridge.core.mission import Mission
import uvicorn

app = FastAPI(title="Living Bridge OS API")
orchestrator = Orchestrator()

@app.post("/mission")
async def create_mission(mission: Mission):
    result = await orchestrator.execute_mission(mission.dict())
    return result

@app.get("/")
async def root():
    return {"message": "Living Bridge OS v0.1 is running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
