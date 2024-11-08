from django.db import models

# Create your models here.

class Proveedor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=125)
    email = models.CharField(unique=True, max_length=125)
    cuenta_pago = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores'



class Categoria(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(max_length=255, blank=True, null=True)
    
    class Meta:
        db_table = 'categorias'

class Producto(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(max_length=255, blank=True, null=True)
    precio = models.PositiveIntegerField(blank=False, null=False, default=999999)
    stock = models.PositiveIntegerField(blank=False, null=False, default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, default=None)
    
    class Meta:
        db_table = 'productos'
    



    
    
    