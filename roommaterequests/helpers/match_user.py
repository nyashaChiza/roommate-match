# accounts/utils/matching.py

from .matching import MatchService

def get_user_match_score(base_user, other_user):
    try:
        service = MatchService(user=base_user)
        score = service.calculate_total_score(candidate=other_user)
        other_user.score = score  # attach dynamically
        return other_user
    except Exception:
        other_user.score = 0.0
        return other_user  # No score if error
