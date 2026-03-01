from pydantic import BaseModel
from typing import List
#student validation schema-Desigaa

class StudentInput(BaseModel):
    name: str
    gpa: float
    skills: List[str]
    interests: List[str]
    resume_text: str