from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

from utils.resume_parser import extract_text
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.ats_scorer import calculate_ats_score
from utils.decision_engine import make_decision

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# -------------------- HOME (ATS PAGE) --------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------- ATS SUBMIT --------------------
@app.route("/submit", methods=["POST"])
def submit():
    resume = request.files.get("resume")
    job_desc = request.form.get("job_desc")

    if not resume or resume.filename == "":
        return "No resume uploaded"

    if not job_desc or not job_desc.strip():
        return "Job description is empty"

    filename = secure_filename(resume.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    resume.save(file_path)

    raw_text = extract_text(file_path)
    cleaned_resume_text = clean_text(raw_text)
    cleaned_jd_text = clean_text(job_desc)

    resume_skills = extract_skills(cleaned_resume_text)
    jd_skills = extract_skills(cleaned_jd_text)

    score, matched = calculate_ats_score(resume_skills, jd_skills)
    decision = make_decision(score)

    return (
        f"ATS Score: {score}%<br>"
        f"Decision: {decision}<br>"
        f"Matched Skills: {', '.join(matched)}"
    )


# -------------------- RUN APP --------------------
if __name__ == "__main__":
    app.run(debug=True)

