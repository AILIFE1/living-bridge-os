from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class Mission(BaseModel):
    objective: str
    constraints: List[str] = []
    agents: List[str] = ["architect", "explorer"]
    context: Optional[Dict[str, Any]] = None

class AgentResponse(BaseModel):
    agent: str
    role: str
    content: str
    timestamp: datetime = datetime.now()

class DebateRound(BaseModel):
    round: int
    responses: List[AgentResponse]

class Consensus(BaseModel):
    agreement: List[str]
    disagreements: List[str]
    consensus: str

class MissionResult(BaseModel):
    mission_id: str
    objective: str
    agent_responses: List[AgentResponse]
    debate: List[DebateRound]
    consensus: Consensus
    artifacts: List[Dict[str, Any]]
    memory_updates: List[Dict[str, Any]]