from django.urls import path
from . import views

urlpatterns = [
    path('anmelden/', views.anmelden, name='anmelden'),
    path('danke/', views.danke, name='danke'),
]
