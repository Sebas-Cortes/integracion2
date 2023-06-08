from django.db import models

# Create your models here.
class Sucursal(models.Model):
    idSucursal = models.AutoField(primary_key=True, verbose_name='Id de las sucursales')
    direccion = models.CharField(max_length=50, blank=False, null=False, verbose_name='Direccion de la sucursal')
    comuna = models.CharField(max_length=50, blank=False, null=False, verbose_name='Comuna de la sucural')
    region = models.CharField(max_length=50, blank=False, null=False, verbose_name='Region de la sucursal')

class Lote(models.Model):
    idLote = models.AutoField(primary_key=True, verbose_name='Id del lote')
    tipo = models.CharField(max_length=30, blank=False, null=False, verbose_name='Tipo de pastillas')
    cantidad = models.IntegerField(blank=False, null=False, verbose_name='Cantidad de pastillas')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

