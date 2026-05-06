from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/', include('eventos.urls')),
    path('recetas/', include('recetas.urls', namespace='recetas')),
]

