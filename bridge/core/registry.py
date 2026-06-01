from typing import Dict, List, Optional
from ..agents.base_agent import BaseAgent
from ..agents.claude_agent import ClaudeAgent
from ..agents.grok_agent import GrokAgent
from ..agents.openai_agent import OpenAIAgent
from ..agents.gemini_agent import GeminiAgent


class AgentRegistry:
    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {}
        self._register_default_agents()

    def _register_default_agents(self):
        self.register(ClaudeAgent())
        self.register(GrokAgent())
        self.register(OpenAIAgent())
        self.register(GeminiAgent())

    def register(self, agent: BaseAgent):
        self.agents[agent.role.lower()] = agent

    def get_agent(self, role: str) -> Optional[BaseAgent]:
        return self.agents.get(role.lower())

    def get_agents(self, agent_roles: List[str] = None) -> List[BaseAgent]:
        if not agent_roles:
            return list(self.agents.values())
        return [self.agents[r.lower()] for r in agent_roles if r.lower() in self.agents]
