from django.contrib import admin
from .models import Teilnehmer, InfoBoxConfig


@admin.register(Teilnehmer)
class TeilnehmerAdmin(admin.ModelAdmin):
    list_display = ['teamname', 'name_kapitaen', 'handy_nr', 'anmeldedatum']
    list_filter = ['anmeldedatum']
    search_fields = ['teamname', 'name_kapitaen']
    ordering = ['-anmeldedatum']


@admin.register(InfoBoxConfig)
class InfoBoxConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Allgemeine Einstellungen', {
            'fields': ('active_mode', 'show_registration_form'),
            'description': 'Wähle den Modus für die Info-Box und ob das Anmeldeformular angezeigt werden soll.'
        }),
        ('Standard Modus', {
            'fields': ('standard_title', 'standard_date', 'standard_fee', 'standard_location', 'standard_team_info', 'standard_contact'),
            'classes': ('collapse',),
            'description': 'Einstellungen für den Standard Turnier-Info Modus'
        }),
        ('Absage Modus', {
            'fields': ('cancelled_title', 'cancelled_message', 'cancelled_contact'),
            'classes': ('collapse',),
            'description': 'Einstellungen für den Turnier-Absage Modus'
        }),
        ('Custom Modus', {
            'fields': ('custom_title', 'custom_content'),
            'classes': ('collapse',),
            'description': 'Einstellungen für den benutzerdefinierten Modus'
        }),
    )
    
    def has_add_permission(self, request):
        # Nur eine Konfiguration erlaubt
        return not InfoBoxConfig.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Konfiguration soll nicht gelöscht werden können
        return False