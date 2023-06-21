from rest_framework import serializers
from core.models import Lote

class LoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ['idLote', 'tipo', 'cantidad', 'sucursal']