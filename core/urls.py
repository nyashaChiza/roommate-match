
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('optimus/', admin.site.urls),
    path('', include('allauth.urls')),
]
