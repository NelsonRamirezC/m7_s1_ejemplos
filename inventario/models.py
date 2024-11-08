from django.db import models


class Categorias(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categorias'
