# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('roommate-requests/', views.roommate_requests_index, name='roommate_requests_index'),
    path('roommate-requests/<int:pk>/', views.roommate_request_detail, name='roommate_request_detail'),
    path('roommate-requests/create/<int:pk>/', views.create_request_view , name='roommate_request_create'),
    path('roommate-requests/<int:pk>/review/', views.roommate_request_review, name='roommate_request_review'),
    path('roommate-requests/<int:pk>/delete/', views.delete_request_view, name='roommate_request_delete'),
]
