from .base_agent import BaseAgent

class OpenAIAgent(BaseAgent):
    role = "Verifier"
    purpose = "Validate reasoning. Check consistency."

    async def process(self, mission):
        return {"response": f"[OpenAI Verifier] Validating: {mission.get('objective')}"}