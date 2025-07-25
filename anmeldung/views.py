
# anmeldung/views.py

from django.shortcuts import render, redirect
from .forms import TeilnehmerForm
from .models import InfoBoxConfig

def anmeldeformular(request):
    # Hole die aktuelle Konfiguration
    config = InfoBoxConfig.get_config()
    
    if request.method == 'POST':
        form = TeilnehmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danke')
    else:
        form = TeilnehmerForm()
    
    context = {
        'form': form,
        'config': config,
    }
    return render(request, 'anmeldung/anmelden.html', context)

def danke(request):
    return render(request, 'anmeldung/danke.html')
