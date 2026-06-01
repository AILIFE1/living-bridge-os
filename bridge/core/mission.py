from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
import uuid

class Mission(BaseModel):
    """Every user request becomes a mission."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    objective: str
    constraints: List[str] = Field(default_factory=list)
    agents: List[str] = Field(default_factory=list)
    status: str = "pending"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
