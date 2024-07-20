from django import forms
from .models import Teilnehmer

class TeilnehmerForm(forms.ModelForm):
    class Meta:
        model = Teilnehmer
        fields = ['teamname', 'name_kapitaen', 'handy_nr']  # Verwende die Feldnamen aus dem Modell
        labels = {
            'teamname': 'Euer Teamname',
            'name_kapitaen': 'Name des Kapitäns',
            'handy_nr': 'Handy-Nummer für Organisation'
        }
        