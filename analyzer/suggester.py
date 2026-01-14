from typing import Set, List


def generate_suggestions(missing_skills: Set[str]) -> List[str]:
    """Creates resume improvement suggestions."""
    suggestions = []

    for skill in missing_skills:
        suggestions.append(f"Consider adding experience with {skill}.")

    return suggestions