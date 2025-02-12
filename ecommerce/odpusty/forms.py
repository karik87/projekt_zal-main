from django import forms
from .models import ZamowienieOdpustu, Klient, Grzesznik, MetodaPlatnosci, Ksiadz, UslugaDodatkowa

class ZamowienieOdpustuForm(forms.ModelForm):
    klient_imie = forms.CharField(max_length=50, label="Twoje imię")
    grzesznik_imie = forms.CharField(max_length=50, label="Imię obdarowanego")
    grzesznik_nazwisko = forms.CharField(max_length=50, label="Nazwisko obdarowanego")

    # Używamy ModelMultipleChoiceField dla ManyToManyField
    uslugi_dodatkowe = forms.ModelMultipleChoiceField(
        queryset=UslugaDodatkowa.objects.all(),
        label="Usługi dodatkowe",
        widget=forms.CheckboxSelectMultiple,  # Pozwala wybrać wiele opcji za pomocą checkboxów
    )

    class Meta:
        model = ZamowienieOdpustu
        fields = ['typ_odpustu', 'ksiadz', 'uslugi_dodatkowe', 'metoda_platnosci']

    def save(self, commit=True):
        klient_imie = self.cleaned_data.pop('klient_imie')
        grzesznik_imie = self.cleaned_data.pop('grzesznik_imie')
        grzesznik_nazwisko = self.cleaned_data.pop('grzesznik_nazwisko')

        klient, _ = Klient.objects.get_or_create(imie=klient_imie)
        grzesznik, _ = Grzesznik.objects.get_or_create(imie=grzesznik_imie, nazwisko=grzesznik_nazwisko)

        zamowienie = super().save(commit=False)
        zamowienie.klient = klient
        zamowienie.grzesznik = grzesznik

        if commit:
            zamowienie.save()
            self.save_m2m()  # Zapisuje ManyToManyField poprawnie

        return zamowienie
