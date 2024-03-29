# Generated by Django 4.2.1 on 2023-06-08 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('idSucursal', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de las sucursales')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion de la sucursal')),
                ('comuna', models.CharField(max_length=50, verbose_name='Comuna de la sucural')),
                ('region', models.CharField(max_length=50, verbose_name='Region de la sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('idLote', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del lote')),
                ('tipo', models.CharField(max_length=30, verbose_name='Tipo de pastillas')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad de pastillas')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sucursal')),
            ],
        ),
    ]
