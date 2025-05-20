from django.urls import path
from .views import (
    add_profile_questions, QuestionListView,
    AnswerCreateView, AnswerListView
)

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='question_list'),
    path('questions/create/', add_profile_questions, name='question_create'),

    path('answers/', AnswerListView.as_view(), name='answer_list'),
    path('answers/create/', AnswerCreateView.as_view(), name='answer_create'),
]
