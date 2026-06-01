from typing import Dict
from .orchestrator import Orchestrator
from ..agents.base_agent import BaseAgent

class AgentRegistry:
    """Registry for managing available agents."""

    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent):
        self.agents[agent.role.lower()] = agent

    def get_orchestrator(self) -> Orchestrator:
        orchestrator = Orchestrator()
        for agent in self.agents.values():
            orchestrator.register_agent(agent)
        return orchestrator
