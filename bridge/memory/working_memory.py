from typing import List, Dict

class WorkingMemory:
    def __init__(self):
        self.interactions: List[Dict] = []

    def add(self, interaction: Dict):
        self.interactions.append(interaction)
        if len(self.interactions) > 20:
            self.interactions.pop(0)

    def get_recent(self) -> List[Dict]:
        return self.interactions