from django.db import models


# Create your models here.
class Crud(models.Model):
    """Crud ejemplo"""

    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=15)
    creditos = models.PositiveSmallIntegerField()

    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)


class SistemaViajes(models.Model):
    """Crud Viajes"""

    num_viaje = models.CharField(primary_key=True, max_length=6)
    articulos = models.CharField(max_length=70)
    hora_entrega_estimado = models.CharField(max_length=5)
    turno = models.PositiveSmallIntegerField()
    direccion = models.CharField(max_length=70)
    num_telefono = models.PositiveSmallIntegerField()


class Manager(models.Model):
    """Crud Manager"""

    codigo_manager = models.CharField(primary_key=True, max_length=1)
    correo = models.CharField(max_length=30)
