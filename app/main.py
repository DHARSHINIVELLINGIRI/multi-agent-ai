import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from .schemas import StudentInput
from .agents import run_orchestrator

app = FastAPI()

# Absolute path to the folder containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
 # Logging initialized by Desigaa
@app.get("/")
async def serve_ui():
    # This points to multi-agent-ai/frontend/index.html
    index_path = os.path.join(BASE_DIR, "..", "frontend", "index.html")
    return FileResponse(index_path)

@app.post("/analyze")
async def analyze_student(data: StudentInput):
    return await run_orchestrator(data)