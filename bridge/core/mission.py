from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class Mission(BaseModel):
    objective: str
    constraints: List[str] = Field(default_factory=list)
    agents: List[str] = Field(default_factory=list)
    status: str = "pending"