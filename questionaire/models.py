from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Question(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questions',
        help_text="The user who owns this question"
    )
    text = models.TextField(help_text="The question to ask potential roommates")
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}: {self.text[:50]}"
    
    def get_questions_for_roommate(self):
        return self.questions.filter(is_active=True)



class Answer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questionnaire_answers',
        help_text="The user answering the question"
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        help_text="The question being answered"
    )
    answer_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'question')

    def __str__(self):
        return f"{self.user.username} answered '{self.question.text[:30]}...'"

