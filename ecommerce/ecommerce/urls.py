from django.contrib import admin
from django.urls import path
from odpusty import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('potwierdzenie/<int:cena>/', views.potwierdzenie, name='potwierdzenie'),
]
