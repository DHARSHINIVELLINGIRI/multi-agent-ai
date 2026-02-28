def skill_gap_agent(data):
    required_skills = ["Python", "DSA", "System Design"]
    missing = [skill for skill in required_skills if skill not in data.skills]
    return {"missing_skills": missing}