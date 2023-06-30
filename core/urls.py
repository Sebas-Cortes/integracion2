from django.urls import path
from core.views import inicio
from django.contrib.auth.views import LogoutView
from .views import finiquitar_res, descontarRes, consultarRes, res, reservarPres, CustomLoginView, descontarPres, addstock, consultaPres, registro, addsucursal, borrarStock, borrarSucursal, finiquitar_pres, pres, stock, sucursal
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', CustomLoginView.as_view(), name="login"),
    path('logout/', login_required(LogoutView.as_view(template_name='core/login.html')), name='logout'),
    path('inicio',login_required(inicio), name="inicio"),
    path('pres',login_required(pres), name="pres"),
    path('finiquitar_pres/<str:rut>',login_required(finiquitar_pres), name="finiquitar_pres"),
    path('stock',login_required(stock), name="stock"),
    path('addstock',login_required(addstock), name="addstock"),
    path('sucursal',login_required(sucursal), name="sucursal"),
    path('addsucursal',login_required(addsucursal), name="addsucursal"),
    path('borrarStock/<int:id>', login_required(borrarStock), name='borrarStock'),
    path('borrarSucursales/<int:id>', login_required(borrarSucursal), name='borrarSucursal'),
    path('registro', login_required(registro), name='registro'),
    path('consultaPres/', login_required(consultaPres), name='consultaPres'),
    path('descontarPres/<str:rut>', login_required(descontarPres), name='descontarPres'),
    path('reservarPres/<str:rut>', login_required(reservarPres), name='reservarPres'),
    path('res',login_required(res), name="res"),
    path('consultaRes/', login_required(consultarRes), name='consultarRes'),
    path('descontarRes/<str:rut>', login_required(descontarRes), name='descontarRes'),
    path('finiquitar_res/<str:rut>',login_required(finiquitar_res), name="finiquitar_res"),
]