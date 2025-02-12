from django.db import models
import random
from django.utils.timezone import now

class Klient(models.Model):
    imie = models.CharField(max_length=50)

    def __str__(self):
        return self.imie

class Grzesznik(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class Ksiadz(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class MetodaPlatnosci(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

class UslugaDodatkowa(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

class ZamowienieOdpustu(models.Model):
    TYP_ODPUSTU_CHOICES = [
        ('cal', 'Odpust Całkowity'),
        ('czes', 'Odpust Częściowy'),
    ]

    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    grzesznik = models.ForeignKey(Grzesznik, on_delete=models.CASCADE)
    typ_odpustu = models.CharField(max_length=4, choices=TYP_ODPUSTU_CHOICES)
    ksiadz = models.ForeignKey(Ksiadz, on_delete=models.CASCADE)
    uslugi_dodatkowe = models.ManyToManyField(UslugaDodatkowa, blank=True)
    metoda_platnosci = models.ForeignKey(MetodaPlatnosci, on_delete=models.CASCADE)
    cena = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_zamowienia = models.DateTimeField(default=now, editable=False)
    wykonane = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.cena:
            self.cena = random.randint(100, 1000)  # Losowa cena
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Zamówienie {self.id} - {self.klient.imie} dla {self.grzesznik.imie} {self.grzesznik.nazwisko}"
