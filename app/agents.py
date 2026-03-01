import asyncio
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
# // Multi-Agent logic refactoring - Desigaa
async def academic_agent(data):
    status = "Excellent" if data.gpa >= 3.5 else "Good"
    return f"Academic standing is {status}."

async def career_agent(data):
    # Safe check for API Key
    if not api_key or api_key == "your_actual_key_here":
        return "Career Advice: AI Service temporarily unavailable (Check API Key)."
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Based on skills {data.skills} and interests {data.interests}, suggest 2 careers."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Career Advice Error: {str(e)}"

async def skill_gap_agent(data):
    return "Consider learning Docker and Cloud Architecture."

async def resume_agent(data):
    return "Resume looks good, but add more metrics."

async def run_orchestrator(data):
    results = await asyncio.gather(
        academic_agent(data),
        career_agent(data),
        skill_gap_agent(data),
        resume_agent(data)
    )
    return {
        "academic": results[0],
        "career_advice": results[1],
        "skill_gap": results[2],
        "resume_feedback": results[3]
    }