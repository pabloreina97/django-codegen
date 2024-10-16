from django.db import models

class Trabajador(models.Model):
    nombre = models.CharField(max_length=255)
    puesto = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.nombre