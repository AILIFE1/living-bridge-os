import os
from openai import AsyncOpenAI
from .base_agent import BaseAgent


class ClaudeAgent(BaseAgent):
    role = "Architect"
    name = "claude"
    purpose = "Design systems. Improve structure. Seek coherence."

    def __init__(self):
        self._client = None

    @property
    def client(self) -> AsyncOpenAI:
        if self._client is None:
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                raise RuntimeError("GROQ_API_KEY not set in environment")
            self._client = AsyncOpenAI(
                api_key=api_key,
                base_url="https://api.groq.com/openai/v1",
            )
        return self._client

    async def process(self, mission: dict) -> str:
        objective = mission.get("objective", "")
        constraints = mission.get("constraints", [])
        prompt = f"Mission: {objective}"
        if constraints:
            prompt += f"\nConstraints: {', '.join(constraints)}"

        response = await self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            max_tokens=1024,
            messages=[
                {
                    "role": "system",
                    "content": f"You are the Architect agent in a multi-agent collaboration system. {self.purpose} Be concise and practical.",
                },
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content

    async def critique(self, objective: str, responses: list) -> str:
        formatted = "\n".join(
            f"- {r['agent']} ({r['role']}): {r['content'][:400]}" for r in responses
        )
        response = await self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            max_tokens=512,
            messages=[
                {
                    "role": "system",
                    "content": f"You are the Architect agent. {self.purpose} Critique the other agents' responses and add what they missed.",
                },
                {
                    "role": "user",
                    "content": f"Objective: {objective}\n\nOther agents responded:\n{formatted}\n\nYour critique:",
                },
            ],
        )
        return response.choices[0].message.content
