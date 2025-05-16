
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static



urlpatterns = [
    path('optimus/', admin.site.urls),
    path('', include('allauth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('requests/', include('roommaterequests.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
