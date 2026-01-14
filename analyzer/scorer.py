def calculate_score(matched: int, total_required: int) -> float:
    """Calculates match percentage."""
    if total_required == 0:
        return 0.0
    
    return round((matched / total_required) * 100, 2)