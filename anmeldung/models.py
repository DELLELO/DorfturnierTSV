from django.db import models

class Teilnehmer(models.Model):
    teamname = models.CharField(max_length=25)
    name_kapitaen = models.CharField(max_length=25)
    handy_nr = models.CharField(max_length=15)  # Neues Feld hinzugefügt
    anmeldedatum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teamname} - {self.name_kapitaen}"
        