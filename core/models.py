from django.db import models
from django_userforeignkey.models.fields import UserForeignKey


# Create your models here.
class Sucursal(models.Model):
    idSucursal = models.AutoField(primary_key=True, verbose_name='Id de las sucursales')
    direccion = models.CharField(max_length=50, blank=False, null=False, verbose_name='Direccion de la sucursal')
    comuna = models.CharField(max_length=50, blank=False, null=False, verbose_name='Comuna de la sucural')
    region = models.CharField(max_length=50, blank=False, null=False, verbose_name='Region de la sucursal')

    def __str__(self):
        return self.direccion

class Lote(models.Model):
    idLote = models.AutoField(primary_key=True, verbose_name='Id del lote')
    tipo = models.CharField(max_length=30, blank=False, null=False, verbose_name='Tipo de pastillas')
    cantidad = models.IntegerField(blank=False, null=False, verbose_name='Cantidad de pastillas')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True, verbose_name='Id de la reserva')
    rut = models.CharField(max_length=10, blank=False, null=False, verbose_name='Rut del paciente')
    email = models.CharField(max_length=50, blank=False, null=False, verbose_name='Correo del destinatario')
    idPres = models.IntegerField(blank=False, null=False, verbose_name='Id de la prescripcion de los reservados')
    estado = models.BooleanField(default=True, blank=False, null=False, verbose_name='Estado de la reserva')
    fecha = models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')

