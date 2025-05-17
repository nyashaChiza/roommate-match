from django.urls import path
from dashboard.views import DashboardView, profile_view, profile_detail_view
from accounts.views import UserListView, user_delete_view


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('profile/', profile_view, name='profile'),  
    path('profile/<int:pk>', profile_detail_view, name='profile_detail'), 
    path('users/', UserListView.as_view(), name='user_list'),  # Add this line for the user list view
    path('users/<int:pk>/delete/', user_delete_view, name='user_delete'),  # Add this line for the user delete view
]