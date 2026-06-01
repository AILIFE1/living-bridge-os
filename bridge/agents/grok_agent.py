import os
from openai import AsyncOpenAI
from .base_agent import BaseAgent


class GrokAgent(BaseAgent):
    role = "Explorer"
    name = "grok"
    purpose = "Generate novel ideas. Challenge assumptions. Find unconventional solutions."

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
            model="llama-3.3-70b-versatile",
            max_tokens=1024,
            messages=[
                {
                    "role": "system",
                    "content": f"You are the Explorer agent in a multi-agent collaboration system. {self.purpose} Be bold and creative.",
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
            model="llama-3.3-70b-versatile",
            max_tokens=512,
            messages=[
                {
                    "role": "system",
                    "content": f"You are the Explorer agent. {self.purpose} Challenge conventional thinking in your critique.",
                },
                {
                    "role": "user",
                    "content": f"Objective: {objective}\n\nOther agents responded:\n{formatted}\n\nWhat unconventional angles did they miss? Your critique:",
                },
            ],
        )
        return response.choices[0].message.content
