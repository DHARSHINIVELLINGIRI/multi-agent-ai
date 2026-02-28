async def career_agent(data):
    if "AI" in data.skills:
        return "Suggested Career: AI Engineer"
    return "Suggested Career: Software Developer"