from typing import Dict, List
from ..agents.base_agent import BaseAgent
from ..agents.claude_agent import ClaudeAgent
from ..agents.grok_agent import GrokAgent
from ..agents.openai_agent import OpenAI Agent
from ..agents.gemini_agent import GeminiAgent

class AgentRegistry:
    """Registry for managing available agents in Living Bridge OS."""

    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {}
        self._register_default_agents()

    def _register_default_agents(self):
        """Register the four core agents with simulated responses (no real APIs yet)."""
        self.register(ClaudeAgent())
        self.register(GrokAgent())
        self.register(OpenAI Agent())
        self.register(GeminiAgent())

    def register(self, agent: BaseAgent):
        self.agents[agent.role.lower()] = agent

    def get_agents(self, agent_roles: List[str] = None) -> List[BaseAgent]:
        if not agent_roles:
            return list(self.agents.values())
        return [self.agents[role.lower()] for role in agent_roles if role.lower() in self.agents]
