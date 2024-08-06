# turnierprojekt/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anmelden/', include('anmeldung.urls')),
]

# django_distill will andreas

