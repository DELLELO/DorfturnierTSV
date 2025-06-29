# anmeldung/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.anmeldeformular, name='formular'),
    path('danke/', views.danke, name='danke'),
]
