def make_decision(score):
    if score >= 70:
        return "Shortlisted"
    elif score >= 40:
        return "Needs Review"
    else:
        return "Rejected"
