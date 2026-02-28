from app.agents.academic_agent import academic_agent
from app.agents.career_agent import career_agent
from app.agents.skill_gap_agent import skill_gap_agent
from app.agents.resume_agent import resume_agent

async def run_agents(data):
    academic = academic_agent(data)
    career = career_agent(data)
    skills = skill_gap_agent(data)
    resume = resume_agent(data)

    return {
        "academic_analysis": academic,
        "career_suggestions": career,
        "skill_gap_analysis": skills,
        "resume_feedback": resume
    }