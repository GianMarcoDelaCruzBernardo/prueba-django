from django.contrib import admin
from .models import Evento, Usuario, RegistroEvento


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'lugar', 'fecha_inicio', 'organizador']
    list_filter = ['categoria', 'fecha_inicio']
    search_fields = ['titulo', 'lugar']


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'correo', 'telefono']
    search_fields = ['nombre', 'correo']


@admin.register(RegistroEvento)
class RegistroEventoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'evento', 'estado', 'fecha_registro']
    list_filter = ['estado']
