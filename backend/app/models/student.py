from pydantic import BaseModel
from typing import List

class StudentInput(BaseModel):
    name: str
    gpa: float
    skills: List[str]
    interests: List[str]
    target_role: str