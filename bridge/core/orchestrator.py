from typing import Dict, Any
from .mission import Mission
from .registry import AgentRegistry
from .debate import DebateEngine
from .synthesis import SynthesisEngine
from bridge.agents.base_agent import BaseAgent
from bridge.agents.claude_agent import ClaudeAgent
from bridge.agents.grok_agent import GrokAgent
from bridge.agents.openai_agent import OpenAIAgent
from bridge.agents.gemini_agent import GeminiAgent

class Orchestrator:
    def __init__(self):
        self.registry = AgentRegistry()
        self.register_default_agents()
        self.debate_engine = DebateEngine()
        self.synthesis_engine = SynthesisEngine()

    def register_default_agents(self):
        self.registry.register_agent("architect", ClaudeAgent)
        self.registry.register_agent("explorer", GrokAgent)
        self.registry.register_agent("verifier", OpenAIAgent)
        self.registry.register_agent("analyst", GeminiAgent)

    async def process_mission(self, mission: Mission) -> Dict[str, Any]:
        # Select agents
        selected_agents = mission.agents or ["architect", "explorer", "verifier", "analyst"]

        responses = {}
        for agent_name in selected_agents:
            agent_class = self.registry.get_agent(agent_name)
            if agent_class:
                agent = agent_class()
                response = await agent.process(mission.dict())
                responses[agent_name] = response

        # Run debate
        debate_result = await self.debate_engine.run_debate(mission, responses)

        # Synthesize
        final_result = self.synthesis_engine.synthesize(responses, debate_result)

        return {
            "mission": mission.dict(),
            "responses": responses,
            "debate": debate_result,
            "consensus": final_result.get("consensus"),
            "status": "completed"
        }