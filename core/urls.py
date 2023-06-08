from django.urls import path
from core.views import inicio
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, addstock, addsucursal, borrarStock, finiquitar_pres, pres, stock, sucursal
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', CustomLoginView.as_view(), name="login"),
    path('logout/', login_required(LogoutView.as_view(template_name='core/login.html')), name='logout'),
    path('inicio',inicio, name="inicio"),
    path('pres',pres, name="pres"),
    path('finiquitar_pres',finiquitar_pres, name="finiquitar_pres"),
    path('stock',stock, name="stock"),
    path('addstock',addstock, name="addstock"),
    path('sucursal',sucursal, name="sucursal"),
    path('addsucursal',addsucursal, name="addsucursal"),
    path('borrarStock/<int:id>', borrarStock, name='borrarStock'),
]