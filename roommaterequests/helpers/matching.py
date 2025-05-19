# accounts/services/matching.py

from django.contrib.auth import get_user_model
from accounts.models import Profile
from questionaire.models import Answer
from django.db.models import Q

User = get_user_model()


class MatchService:
    def __init__(self, user):
        self.user = user
        self.user_profile = getattr(user, 'profile', None)
        self.user_answers = {a.question_id: a.answer_text for a in Answer.objects.filter(user=user)}

    def get_candidates(self):
        """
        Return other users who are potential roommates.
        You can customize filtering here to exclude blocked users, incompatible user types, etc.
        """
        return User.objects.exclude(id=self.user.id).select_related('profile')

    def calculate_total_score(self, candidate, weights=None):
        """
        Calculates the total match score between self.user and a candidate.
        The score is normalized between 0.0 and 1.0.
        """
        if not self.user_profile or not hasattr(candidate, 'profile'):
            raise ValueError("Missing profile for scoring")

        profile = candidate.profile
        total = 0
        max_score = 0

        # Default weights for attributes (adjust as needed)
        default_weights = {
            'sleep_schedule': 1,
            'cleanliness_level': 1,
            'social_habits': 1,
            'study_preference': 1,
            'questionnaire': 2
        }

        weights = weights or default_weights

        # Profile attributes match (categorical comparison)
        for attr in ['sleep_schedule', 'cleanliness_level', 'social_habits', 'study_preference']:
            max_score += weights[attr]
            if getattr(self.user_profile, attr) and getattr(profile, attr):
                if getattr(self.user_profile, attr) == getattr(profile, attr):
                    total += weights[attr]

        # Questionnaire matching
        max_score += weights['questionnaire']
        match_count = 0
        total_questions = 0

        for answer in Answer.objects.filter(user=candidate):
            if answer.question_id in self.user_answers:
                total_questions += 1
                if self.user_answers[answer.question_id].strip().lower() == answer.answer_text.strip().lower():
                    match_count += 1

        if total_questions > 0:
            total += (match_count / total_questions) * weights['questionnaire']

        if max_score == 0:
            return 0.0

        return round(total / max_score, 2)

    def get_ranked_matches(self, min_score=0.5):
        """
        Returns a list of candidate users with a `score` attribute.
        """
        candidates = self.get_candidates()
        scored_candidates = []

        for candidate in candidates:
            try:
                score = self.calculate_total_score(candidate)
                if score >= min_score:
                    candidate.score = score  # dynamic attribute for rendering
                    scored_candidates.append(candidate)
            except Exception:
                continue

        return sorted(scored_candidates, key=lambda c: c.score, reverse=True)
