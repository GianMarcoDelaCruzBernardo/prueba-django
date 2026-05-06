from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('evento/<int:pk>/', views.detalle_evento, name='detalle_evento'),
    path('evento/crear/', views.crear_evento, name='crear_evento'),
    path('evento/<int:pk>/editar/', views.editar_evento, name='editar_evento'),
    path('evento/<int:pk>/eliminar/', views.eliminar_evento, name='eliminar_evento'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('registro/crear/', views.registrar_usuario, name='registrar_usuario'),
    path('registro/<int:pk>/eliminar/', views.eliminar_registro, name='eliminar_registro'),
    path('consultas/', views.consultas_avanzadas, name='consultas_avanzadas'),
]
