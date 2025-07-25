from django.db import models

class Teilnehmer(models.Model):
    teamname = models.CharField(max_length=25)
    name_kapitaen = models.CharField(max_length=25)
    handy_nr = models.CharField(max_length=15)  # Neues Feld hinzugefügt
    anmeldedatum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teamname} - {self.name_kapitaen}"


class InfoBoxConfig(models.Model):
    """Konfiguration für die Info-Box auf der Anmeldeseite"""
    
    MODE_CHOICES = [
        ('standard', 'Standard Turnier Info'),
        ('cancelled', 'Turnier Absage'),
        ('custom', 'Benutzerdefiniert'),
    ]
    
    # Es sollte nur eine Konfiguration geben
    active_mode = models.CharField(
        max_length=20, 
        choices=MODE_CHOICES, 
        default='standard',
        verbose_name="Aktiver Modus"
    )
    
    # Standard Modus Felder
    standard_title = models.CharField(
        max_length=100, 
        default="Info", 
        verbose_name="Standard: Titel"
    )
    standard_date = models.CharField(
        max_length=100, 
        default="Samstag, 26.07.2025", 
        verbose_name="Standard: Datum"
    )
    standard_fee = models.CharField(
        max_length=100, 
        default="10€ Startgebühr", 
        verbose_name="Standard: Startgebühr"
    )
    standard_location = models.CharField(
        max_length=200, 
        default="Am Starzenbach, 82340 Feldafing", 
        verbose_name="Standard: Ort"
    )
    standard_team_info = models.CharField(
        max_length=100, 
        default="4+1 Spieler Pro Team", 
        verbose_name="Standard: Team Info"
    )
    standard_contact = models.TextField(
        default="Fragen?\n-> +49 176 8513 1778", 
        verbose_name="Standard: Kontakt"
    )
    
    # Absage Modus Felder
    cancelled_title = models.CharField(
        max_length=100, 
        default="Turnier Absage", 
        verbose_name="Absage: Titel"
    )
    cancelled_message = models.TextField(
        default="Dieses Jahr findet das Dorfturnier leider nicht statt aufgrund zu wenig Anmeldungen.\n\nWir hoffen auf nächstes Jahr!", 
        verbose_name="Absage: Nachricht"
    )
    cancelled_contact = models.TextField(
        default="Fragen?\n-> +49 176 8513 1778", 
        verbose_name="Absage: Kontakt"
    )
    
    # Custom Modus Felder
    custom_title = models.CharField(
        max_length=100, 
        default="Info", 
        verbose_name="Custom: Titel"
    )
    custom_content = models.TextField(
        default="Hier kann beliebiger Inhalt stehen.", 
        verbose_name="Custom: Inhalt",
        help_text="HTML-Tags sind erlaubt. Zeilenumbrüche mit <br> erstellen."
    )
    
    # Zusätzliche Einstellungen
    show_registration_form = models.BooleanField(
        default=True, 
        verbose_name="Anmeldeformular anzeigen",
        help_text="Wenn deaktiviert, wird nur die Info-Box angezeigt"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Info-Box Konfiguration"
        verbose_name_plural = "Info-Box Konfiguration"
    
    def __str__(self):
        return f"Info-Box Config ({self.get_active_mode_display()})"
    
    def save(self, *args, **kwargs):
        # Stelle sicher, dass nur eine Konfiguration existiert
        if not self.pk and InfoBoxConfig.objects.exists():
            # Aktualisiere die bestehende Konfiguration anstatt eine neue zu erstellen
            existing = InfoBoxConfig.objects.first()
            existing.active_mode = self.active_mode
            existing.save()
            return existing
        super().save(*args, **kwargs)
    
    @classmethod
    def get_config(cls):
        """Holt die aktuelle Konfiguration oder erstellt eine Standard-Konfiguration"""
        config, created = cls.objects.get_or_create(pk=1)
        return config
        