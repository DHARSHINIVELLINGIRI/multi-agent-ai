from fastapi import FastAPI
from .schemas import StudentInput
from .agents import run_orchestrator

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "Multi-Agent AI is running"}

@app.post("/analyze")
async def analyze_student(data: StudentInput):
    return await run_orchestrator(data)