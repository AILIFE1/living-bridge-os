from bridge.core.mission import Mission
from bridge.core.registry import AgentRegistry
from bridge.core.debate import DebateEngine
from bridge.core.synthesis import SynthesisEngine
from bridge.core.database import SessionLocal, init_db
from bridge.memory.working_memory import WorkingMemory
from typing import Dict, Any
import uuid
from datetime import datetime

class Orchestrator:
    def __init__(self):
        init_db()
        self.db = SessionLocal()
        self.registry = AgentRegistry()
        self.debate_engine = DebateEngine()
        self.synthesis_engine = SynthesisEngine()
        self.working_memory = WorkingMemory()

    async def execute_mission(self, mission_data: dict) -> Dict[str, Any]:
        mission = Mission(**mission_data)
        if not mission.id:
            mission.id = str(uuid.uuid4())
        
        # Register mission in working memory
        self.working_memory.add_interaction(f"Mission started: {mission.objective}")
        
        # Select and dispatch to agents
        agents = self.registry.get_agents(mission.agents)
        responses = []
        for agent in agents:
            response = await agent.process(mission.dict())
            responses.append(response)
        
        # Run debate
        debate_result = self.debate_engine.run_debate(responses)
        
        # Synthesize consensus
        consensus = self.synthesis_engine.generate_consensus(debate_result)
        
        # Create artifact (simulated)
        artifact = {
            "id": str(uuid.uuid4()),
            "type": "consensus",
            "title": f"Consensus for {mission.objective}",
            "content": consensus
        }
        
        # Store in memory and DB (simulated for now)
        self.working_memory.add_interaction(f"Consensus reached for mission {mission.id}")
        
        result = {
            "mission_id": mission.id,
            "objective": mission.objective,
            "status": "completed",
            "agent_responses": [r.dict() for r in responses],
            "debate": debate_result,
            "consensus": consensus,
            "artifact": artifact,
            "timestamp": datetime.now().isoformat()
        }
        
        return result
