from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class Mission(BaseModel):
    id: Optional[str] = None
    objective: str
    constraints: List[str] = []
    agents: List[str] = ["architect", "explorer", "verifier", "analyst"]
    status: str = "pending"
    created_at: datetime = datetime.now()
    result: Optional[Dict[str, Any]] = None

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}
