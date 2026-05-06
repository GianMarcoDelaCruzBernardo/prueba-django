from django.urls import path
from . import views

app_name = 'recetas'

urlpatterns = [
    path('',                    views.lista_recetas,    name='lista'),
    path('nueva/',              views.nueva_receta,     name='nueva'),
    path('<int:pk>/',           views.detalle_receta,   name='detalle'),
    path('<int:pk>/editar/',    views.editar_receta,    name='editar'),
    path('<int:pk>/eliminar/',  views.eliminar_receta,  name='eliminar'),
    path('autores/',            views.lista_autores,    name='autores'),
    path('autores/nuevo/',      views.nuevo_autor,      name='nuevo_autor'),
]
