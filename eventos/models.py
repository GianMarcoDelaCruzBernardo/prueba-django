from django.db import models


class Usuario(models.Model):
    """Modelo que representa a un usuario del sistema de eventos."""
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def _str_(self):
        return self.nombre

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Evento(models.Model):
    """Modelo que representa un evento."""
    CATEGORIAS = [
        ('CONFERENCIA', 'Conferencia'),
        ('TALLER', 'Taller'),
        ('SEMINARIO', 'Seminario'),
        ('WEBINAR', 'Webinar'),
    ]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    capacidad_maxima = models.PositiveIntegerField(default=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='CONFERENCIA')
    organizador = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='eventos_organizados'
    )

    def _str_(self):
        return self.titulo

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['fecha_inicio']


class RegistroEvento(models.Model):
    """Modelo que representa el registro de un usuario en un evento."""
    ESTADOS = [
        ('CONFIRMADO', 'Confirmado'),
        ('PENDIENTE', 'Pendiente'),
        ('CANCELADO', 'Cancelado'),
    ]
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='registros'
    )
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='registros'
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='CONFIRMADO')

    def _str_(self):
        return f"{self.usuario} -> {self.evento}"

    class Meta:
        verbose_name = "Registro de Evento"
        verbose_name_plural = "Registros de Eventos"
        unique_together = ('usuario', 'evento')
