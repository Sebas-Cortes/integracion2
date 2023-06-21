from django.shortcuts import render
from api.serializers import LoteSerializers
from rest_framework.decorators import api_view, permission_classes
from core.models import Lote
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt

@api_view(['GET'])
def lote(request):
    if request.method == 'GET':
        LineUps = Lote.objects.all()
        serializer = LoteSerializers(LineUps,many=True)
        return Response(serializer.data)
