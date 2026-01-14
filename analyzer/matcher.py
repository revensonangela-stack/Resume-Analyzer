from typing import Set, Dict

def match_skills(resume_skills: Set[str], jd_skills: Set[str]) -> Dict[str, Set[str]]:
    """Compares resume skills with job description skills."""
    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills - resume_skills

    return {
    "matched": matched,
    "missing": missing
    }