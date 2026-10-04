
def calculate_match_score(user_skills: list[str], job_skills: list[str]) -> float:
    if not job_skills:
        return 0.0

    user_skill_set = {skill.strip().lower() for skill in user_skills if skill and skill.strip()}
    job_skill_set = {skill.strip().lower() for skill in job_skills if skill and skill.strip()}

    if not job_skill_set:
        return 0.0

    matched_skills = user_skill_set.intersection(job_skill_set)
    return (len(matched_skills) / len(job_skill_set)) * 100.0
