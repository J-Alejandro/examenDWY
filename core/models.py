from django.db import models

# Create your models here.

class Tienda(models.Model):
    #id
    nombreTienda = models.CharField(max_length=150)
    nombreSucursal = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=150)
    region = models.CharField(max_length=150)

    def __str__(self):
        return self.nombreTienda
        
    class Meta:
        verbose_name = "Tienda"
        verbose_name_plural = "Tiendas"

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=150)
    costoPresupuestado = models.IntegerField()
    costoReal = models.IntegerField()
    tienda = (('Seleccionar','Seleccionar'),('PcFactoria','PcFactoria'),('ABCFunciona','ABCFunciona'),('Me109cito','Me109cito'))
    tienda = models.CharField(max_length=50,choices=tienda,default="Seleccionar",verbose_name='Tienda')
    notaAdicional = models.CharField(max_length=150)

    def __str__(self):
        return self.nombreProducto

    class  Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"