from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

class UserRequest(BaseModel):
    query: str
class StudentInput(BaseModel):
    name: str
    gpa: float
    skills: list[str]
    interests: list[str]
    resume_text: str

@app.post("/analyze")
async def analyze_student(data: StudentInput):
    result = await run_agents(data)
    return result

@app.get("/")
def root():
    return {"message": "Multi-Agent AI Backend is running 🚀"}

@app.post("/ask")
def ask_ai(request: UserRequest):
    try:
        user_query = request.query

        response = client.models.generate_content(
            model="gemini-2.5-flash",   # ✅ Correct model
            contents=user_query        # ✅ Plain string
        )

        return {
            "query": user_query,
            "response": response.text
        }

    except Exception as e:
        return {"error": str(e)}