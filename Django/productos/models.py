from django.db import models
from django.utils import timezone
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)  # candena de texto limitada

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # CASCADE:eliminar el producto
    # PROTECT: lanza un error
    # RESTRICT: solo elimina si no existen productos
    # SET_NULL: actualiza a valor nulo
    # SET_DEFAULT:asgina el valor por defecto

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE)  # referencia a otra clase

# actualizar de manera automaticad
    creado_en = models.DateTimeField(default=timezone.now)
