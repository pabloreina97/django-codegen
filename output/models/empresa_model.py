from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    nif = models.CharField(max_length=30)
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre