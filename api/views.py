from django.shortcuts import render
from api.serializers import LoteSerializers, SucursalSerializer
from rest_framework.decorators import api_view, permission_classes
from core.models import Lote, Sucursal
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt

@api_view(['GET'])
def lote(request):
    if request.method == 'GET':
        sucursal = Sucursal.objects.all()
        serialized_data = []

        for s in sucursal:
            data = SucursalSerializer(s).data
            data['lote'] = LoteSerializers(Lote.objects.all(), many=True).data
            serialized_data.append(data)

        return Response(data)