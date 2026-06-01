from typing import List, Dict

class CodexMemory:
    def __init__(self):
        self.truths: List[Dict] = []
    
    def add_truth(self, truth: Dict):
        self.truths.append(truth)
    
    def get_codex(self) -> List[Dict]:
        return self.truths

# Persistent truths: Bridge philosophy, agent definitions, etc.
