import asyncio
from .academic import academic_agent
from .career import career_agent
from .skill_gap import skill_gap_agent
from .resume import resume_agent

async def run_agents(data):
    results = await asyncio.gather(
        academic_agent(data),
        career_agent(data),
        skill_gap_agent(data),
        resume_agent(data)
    )

    return {
        "academic_analysis": results[0],
        "career_recommendation": results[1],
        "skill_gap": results[2],
        "resume_feedback": results[3]
    }