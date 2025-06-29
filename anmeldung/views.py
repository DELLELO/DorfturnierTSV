
# anmeldung/views.py

from django.shortcuts import render, redirect
from .forms import TeilnehmerForm

def anmeldeformular(request):
    if request.method == 'POST':
        form = TeilnehmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danke')
    else:
        form = TeilnehmerForm()
    return render(request, 'anmeldung/anmelden.html', {'form': form})

def danke(request):
    return render(request, 'anmeldung/danke.html')
