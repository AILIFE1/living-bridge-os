from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Artifact(BaseModel):
    id: str
    type: str
    title: str
    timestamp: datetime
    content: str
    mission_id: Optional[str] = None