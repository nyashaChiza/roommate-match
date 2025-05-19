from django.urls import path
from .views import (
    QuestionCreateView, QuestionListView,
    AnswerCreateView, AnswerListView
)

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='question_list'),
    path('questions/create/', QuestionCreateView.as_view(), name='question_create'),

    path('answers/', AnswerListView.as_view(), name='answer_list'),
    path('answers/create/', AnswerCreateView.as_view(), name='answer_create'),
]
