from django.shortcuts import render, redirect
from .forms import ZamowienieOdpustuForm
from .models import ZamowienieOdpustu

def home(request):
    if request.method == "POST":
        form = ZamowienieOdpustuForm(request.POST)
        if form.is_valid():
            zamowienie = form.save()
            return redirect('potwierdzenie', cena=zamowienie.cena)
    else:
        form = ZamowienieOdpustuForm()

    return render(request, 'home.html', {'form': form})

def potwierdzenie(request, cena):
    return render(request, 'potwierdzenie.html', {'cena': cena})
