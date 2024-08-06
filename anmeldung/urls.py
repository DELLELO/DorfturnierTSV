# anmeldung/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.anmelden, name='anmelden'),
    path('danke/', views.danke, name='danke'),
]
