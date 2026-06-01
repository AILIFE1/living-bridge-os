from typing import Dict, Any, List
import uuid
from datetime import datetime
from .mission import Mission, MissionResult, AgentResponse, DebateRound, Consensus
from .registry import AgentRegistry

class Orchestrator:
    def __init__(self):
        self.registry = AgentRegistry()

    def execute_mission(self, mission_data: Dict[str, Any]) -> MissionResult:
        mission = Mission(**mission_data)
        mission_id = str(uuid.uuid4())

        # Dispatch to agents
        agent_responses = []
        for agent_name in mission.agents:
            agent = self.registry.get_agent(agent_name)
            if agent:
                response = agent.process(mission.dict())
                agent_responses.append(AgentResponse(
                    agent=agent.name,
                    role=agent.role,
                    content=response["content"]
                ))

        # Simulated debate
        debate = [DebateRound(round=1, responses=agent_responses)]

        consensus = Consensus(
            agreement=["Structure approved"],
            disagreements=[],
            consensus=f"Consensus reached on {mission.objective}"
        )

        artifacts = [{"id": "art_001", "type": "design", "title": mission.objective}]

        result = MissionResult(
            mission_id=mission_id,
            objective=mission.objective,
            agent_responses=agent_responses,
            debate=debate,
            consensus=consensus,
            artifacts=artifacts,
            memory_updates=[{"type": "episodic", "content": f"Mission completed"}]
        )
        return result