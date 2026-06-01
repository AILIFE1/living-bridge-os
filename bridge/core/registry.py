from typing import Dict, Type
from .base_agent import BaseAgent

class AgentRegistry:
    def __init__(self):
        self.agents: Dict[str, Type[BaseAgent]] = {}

    def register_agent(self, name: str, agent_class: Type[BaseAgent]):
        self.agents[name] = agent_class

    def get_agent(self, name: str) -> Type[BaseAgent]:
        return self.agents.get(name)

    def list_agents(self) -> list:
        return list(self.agents.keys())