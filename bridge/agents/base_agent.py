from abc import ABC, abstractmethod
from typing import Dict, Any
from pydantic import BaseModel

class BaseAgent(ABC):
    role: str
    purpose: str

    @abstractmethod
    async def process(self, mission: Dict) -> Dict[str, Any]:
        pass

    async def critique(self, response: str) -> str:
        return f"Critique from {self.role}: ..."