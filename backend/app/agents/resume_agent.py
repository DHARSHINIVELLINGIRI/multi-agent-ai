async def resume_agent(data):
    if len(data.resume_text) < 100:
        return "Expand your resume content."
    return "Resume looks detailed."