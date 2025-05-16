from django.urls import path
from dashboard.views import DashboardView, profile_view, profile_detail_view


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('profile/', profile_view, name='profile'),  
    path('profile/<int:pk>', profile_detail_view, name='profile_detail'), 
]