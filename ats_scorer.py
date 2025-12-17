def calculate_ats_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0

    matched_skills = set(resume_skills).intersection(set(jd_skills))
    score = (len(matched_skills) / len(jd_skills)) * 100

    return round(score, 2), list(matched_skills)
