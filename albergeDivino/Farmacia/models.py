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

class AsignacionSuministro(models.Model):
    asignado_a = models.CharField(max_length=100)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(default=timezone.now)
    cantidad = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        medicamento = self.medicamento
        medicamento.cantidad -= self.cantidad
        medicamento.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Asignación de Suministro"
        verbose_name_plural = "Asignaciones de Suministro"
        ordering = ["-fecha_asignacion"]

    def __str__(self):
        return f"{self.asignado_a}, {self.medicamento.nombre}"
