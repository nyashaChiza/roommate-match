from django.urls import path
from .views import (
    add_profile_questions, QuestionListView,
    answer_questions_for_profile, AnswerListView
)

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='question_list'),
    path('questions/create/', add_profile_questions, name='question_create'),

    path('answers/', AnswerListView.as_view(), name='answer_list'),
    path('roommate-request/<int:pk>/review/', answer_questions_for_profile, name='answer_create'),
]
