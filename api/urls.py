from django.urls import path
from api.views import lote

urlpatterns = [
    path('Lote/', lote, name="Lote")
]