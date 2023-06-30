from rest_framework import serializers
from core.models import Lote, Sucursal

class LoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ['idLote', 'tipo', 'cantidad']

class SucursalSerializer(serializers.ModelSerializer):
    lote = LoteSerializers(many = True, read_only = True)

    class Meta:
        model = Sucursal
        fields = ['direccion', 'comuna', 'region', 'lote']