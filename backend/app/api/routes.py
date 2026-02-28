from fastapi import APIRouter
from app.models.student import StudentInput
from app.agents.orchestrator import run_agents

router = APIRouter()

@router.post("/analyze")
async def analyze_student(data: StudentInput):
    result = await run_agents(data)
    return result