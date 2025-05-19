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
        return User.objects.exclude(id=self.user.id).select_related('profile')

    def calculate_total_score(self, candidate, weights=None):
        if not self.user_profile or not hasattr(candidate, 'profile'):
            raise ValueError("Missing profile for scoring")

        profile = candidate.profile
        total = 0
        max_score = 0

        # Attributes to compare
        attributes = [
            'sleep_schedule',
            'cleanliness_level',
            'social_habits',
            'study_preference',
            'noise_tolerance',
            'cooking_frequency',
            'guest_policy',
            'pet_preference',
            'smoking_preference',
        ]

        # Default weights
        default_weights = {attr: 1 for attr in attributes}
        default_weights['questionnaire'] = 2

        weights = weights or default_weights

        # Compare profile attributes
        for attr in attributes:
            max_score += weights.get(attr, 1)
            user_value = getattr(self.user_profile, attr, None)
            candidate_value = getattr(profile, attr, None)
            if user_value and candidate_value and user_value == candidate_value:
                total += weights.get(attr, 1)

        # Questionnaire score
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
        candidates = self.get_candidates()
        scored_candidates = []

        for candidate in candidates:
            try:
                score = self.calculate_total_score(candidate)
                if score >= min_score:
                    candidate.score = score  # Attach score dynamically
                    scored_candidates.append(candidate)
            except Exception:
                continue

        return sorted(scored_candidates, key=lambda c: c.score, reverse=True)
