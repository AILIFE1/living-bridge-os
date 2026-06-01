import asyncio
import uuid
from typing import Dict, Any
from datetime import datetime
from .mission import Mission, MissionResult, AgentResponse, DebateRound, Consensus
from .registry import AgentRegistry
from .database import SessionLocal, MissionDB, init_db


class Orchestrator:
    def __init__(self):
        self.registry = AgentRegistry()
        init_db()

    async def execute_mission(self, mission_data: Dict[str, Any]) -> MissionResult:
        mission = Mission(**mission_data)
        mission_id = str(uuid.uuid4())

        agents = self.registry.get_agents(mission.agents)
        if not agents:
            raise ValueError(f"No agents found for roles: {mission.agents}")

        # Round 1: all agents respond to the mission
        results = await asyncio.gather(
            *[agent.process(mission_data) for agent in agents],
            return_exceptions=True,
        )

        round1_responses = []
        for agent, result in zip(agents, results):
            content = result if isinstance(result, str) else f"[Error: {result}]"
            round1_responses.append(
                AgentResponse(agent=agent.name, role=agent.role, content=content)
            )

        # Round 2: agents critique each other's round-1 responses
        responses_for_critique = [
            {"agent": r.agent, "role": r.role, "content": r.content}
            for r in round1_responses
        ]
        critiques = await asyncio.gather(
            *[
                agent.critique(
                    mission.objective,
                    [r for r in responses_for_critique if r["agent"] != agent.name],
                )
                for agent in agents
            ],
            return_exceptions=True,
        )

        round2_responses = []
        for agent, critique in zip(agents, critiques):
            content = critique if isinstance(critique, str) else f"[Error: {critique}]"
            round2_responses.append(
                AgentResponse(agent=agent.name, role=agent.role, content=content)
            )

        consensus = Consensus(
            agreement=[
                f"Mission '{mission.objective}' addressed from {len(agents)} perspectives across 2 debate rounds"
            ],
            disagreements=[],
            consensus=round1_responses[0].content[:300] if round1_responses else "",
        )

        result = MissionResult(
            mission_id=mission_id,
            objective=mission.objective,
            agent_responses=round1_responses,
            debate=[
                DebateRound(round=1, responses=round1_responses),
                DebateRound(round=2, responses=round2_responses),
            ],
            consensus=consensus,
            artifacts=[{"id": f"art_{mission_id[:8]}", "type": "debate", "title": mission.objective}],
            memory_updates=[{"type": "episodic", "content": f"Mission completed: {mission.objective}"}],
        )

        # Persist to DB
        db = SessionLocal()
        try:
            db.add(MissionDB(objective=mission.objective, status="completed", data=result.model_dump(mode="json")))
            db.commit()
        finally:
            db.close()

        return result
