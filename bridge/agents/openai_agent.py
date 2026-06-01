from .base_agent import BaseAgent


class OpenAIAgent(BaseAgent):
    role = "Verifier"
    name = "openai"
    purpose = "Validate reasoning. Check consistency."

    async def process(self, mission: dict) -> str:
        return f"[Verifier stub] OpenAI API not wired yet. Objective: {mission.get('objective')}"

    async def critique(self, objective: str, responses: list) -> str:
        return "[Verifier stub] OpenAI API not wired yet."
