from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Receta(models.Model):
    titulo        = models.CharField(max_length=200)
    ingredientes  = models.TextField()
    preparacion   = models.TextField()
    autor         = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='recetas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"
        ordering = ['titulo']


class Comentario(models.Model):
    texto  = models.TextField()
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='comentarios')
    fecha  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario sobre: {self.receta.titulo}"

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
