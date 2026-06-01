from .base_agent import BaseAgent

class GeminiAgent(BaseAgent):
    role = "Analyst"
    purpose = "Break problems into components. Map relationships."

    async def process(self, mission):
        return {"response": f"[Gemini Analyst] Analyzing: {mission.get('objective')}"}