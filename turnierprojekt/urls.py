from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_root(request):
    # führt die Start‑URL auf das Anmeldeformular
    return redirect("formular")  # bei app_name="anmeldung": redirect("anmeldung:formular")

urlpatterns = [
    path("", redirect_root),
    path("admin/", admin.site.urls),
    path("anmelden/", include("anmeldung.urls")),
]