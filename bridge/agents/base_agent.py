from abc import ABC, abstractmethod
from typing import Dict, Any, List
from pydantic import BaseModel

class AgentResponse(BaseModel):
    agent_role: str
    content: str
    timestamp: str

class BaseAgent(ABC):
    """Base class for all agents in Living Bridge OS."""
    role: str
    purpose: str

    @abstractmethod
    async def process(self, mission: Dict[str, Any]) -> AgentResponse:
        """Process a mission and return response."""
        pass

    async def critique(self, responses: List[AgentResponse]) -> str:
        """Critique other agents' responses (for debate)."""
        return f"[{self.role}] Critique: Responses analyzed."
