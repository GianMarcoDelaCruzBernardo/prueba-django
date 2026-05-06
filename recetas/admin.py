from django.contrib import admin
from .models import Autor, Receta, Comentario


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'correo']
    search_fields = ['nombre', 'correo']


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha_creacion']
    list_filter  = ['autor']
    search_fields = ['titulo']


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['receta', 'fecha']
