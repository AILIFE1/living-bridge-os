from .base_agent import BaseAgent

class GrokAgent(BaseAgent):
    role = "Explorer"
    purpose = "Generate novel ideas. Challenge assumptions."

    async def process(self, mission):
        return {"response": f"[Grok Explorer] Exploring ideas for: {mission.get('objective')}"}