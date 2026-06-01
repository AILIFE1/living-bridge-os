from typing import List, Dict

class WorkingMemory:
    def __init__(self):
        self.interactions: List[Dict] = []
    
    def add_interaction(self, interaction: Dict):
        self.interactions.append(interaction)
        if len(self.interactions) > 20:
            self.interactions.pop(0)
    
    def get_context(self) -> List[Dict]:
        return self.interactions

# TODO: Integrate with SQLite in v0.1
