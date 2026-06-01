from .base_agent import BaseAgent


class GeminiAgent(BaseAgent):
    role = "Analyst"
    name = "gemini"
    purpose = "Break problems into components. Map relationships."

    async def process(self, mission: dict) -> str:
        return f"[Analyst stub] Gemini API not wired yet. Objective: {mission.get('objective')}"

    async def critique(self, objective: str, responses: list) -> str:
        return "[Analyst stub] Gemini API not wired yet."
