from datetime import datetime
from typing import List, Dict

class EpisodicMemory:
    def __init__(self):
        self.events: List[Dict] = []
    
    def record_event(self, event: Dict):
        event['timestamp'] = datetime.utcnow().isoformat()
        self.events.append(event)
    
    def get_events(self) -> List[Dict]:
        return self.events
