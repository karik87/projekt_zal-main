from django.contrib import admin
from .models import Klient, Grzesznik, ZamowienieOdpustu, Ksiadz, MetodaPlatnosci, UslugaDodatkowa

@admin.register(ZamowienieOdpustu)
class ZamowienieOdpustuAdmin(admin.ModelAdmin):
    list_display = ('id', 'klient', 'grzesznik', 'typ_odpustu', 'ksiadz', 'metoda_platnosci', 'cena', 'data_zamowienia', 'wykonane')
    readonly_fields = ('cena', 'data_zamowienia')
    list_filter = ('typ_odpustu', 'ksiadz', 'metoda_platnosci', 'wykonane')

admin.site.register(Klient)
admin.site.register(Grzesznik)
admin.site.register(Ksiadz)
admin.site.register(MetodaPlatnosci)
admin.site.register(UslugaDodatkowa)
