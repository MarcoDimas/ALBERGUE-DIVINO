from django.db import models
from django.utils import timezone

class Medicamento(models.Model):
    categoria = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_caducidad = models.DateField()
    cantidad = models.IntegerField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre
