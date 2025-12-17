import re

def normalize(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text.strip()

def extract_skills(text):
    skills_db = [
        "python", "java", "sql", "html", "css",
        "javascript", "react", "node", "express",
        "machine learning", "deep learning", "artificial intelligence",
        "data science", "flask", "django", "fastapi",
        "numpy", "pandas", "scikit learn", "tensorflow",
        "pytorch", "mysql", "postgresql", "mongodb"
    ]

    text = normalize(text)

    found_skills = []

    for skill in skills_db:
        skill_norm = normalize(skill)
        if skill_norm in text:
            found_skills.append(skill)

    return list(set(found_skills))


