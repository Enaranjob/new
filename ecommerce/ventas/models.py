from django.db import models
from datetime import datetime,date

class Grupo(models.Model):
    descripcion = models.CharField(max_length=100, blank=True, null=True,unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        ordering = ['descripcion']

    def __str__(self):
        return "{}".format(self.descripcion)

class Articulo(models.Model):
    descripcion = models.CharField(verbose_name='Nombre',max_length=100,unique=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    imagen = models.ImageField(db_column="foto", upload_to='articulo/%Y/%m/%d', null=True, blank=True)
    stock = models.IntegerField('Stock',default=0)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')
    fecha_caducidad = models.DateField(default=date.today())
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['id']

    def __str__(self):
        return self.descripcion
