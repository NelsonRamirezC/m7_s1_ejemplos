from django.db import models

class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'
        
class Proveedor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=125)
    email = models.CharField(unique=True, max_length=125)
    cuenta_pago = models.CharField(max_length=20, blank=True, null=True)
    descuento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores'



class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'productos'

