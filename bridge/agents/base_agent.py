from abc import ABC, abstractmethod
from typing import Dict, Any, List


class BaseAgent(ABC):
    role: str
    name: str
    purpose: str

    @abstractmethod
    async def process(self, mission: Dict[str, Any]) -> str:
        pass

    async def critique(self, objective: str, responses: List[Dict[str, str]]) -> str:
        return f"[{self.role}] No critique implemented."
