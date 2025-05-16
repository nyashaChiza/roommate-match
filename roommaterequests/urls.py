# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('roommate-requests/', views.roommate_requests_index, name='roommate_requests_index'),
    path('roommate-requests/<int:pk>/', views.roommate_request_detail, name='roommate_request_detail'),
]
