from django.db import models

class Factura(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    num_factura = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return f'Factura {self.num_factura} - {self.empresa.nombre}'