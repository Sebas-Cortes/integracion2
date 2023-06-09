from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from core.forms import LoginForm, LoteForm, SucursalForm, UserForm
from core.models import Lote, Sucursal
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
def login(request):
    return render(request, 'core/login.html')

class CustomLoginView(LoginView):
    template_name = "core/login.html"
    form_class = LoginForm

def inicio (request):
    return render (request,'core/inicio.html')
def sucursal (request):
    sucursal = Sucursal.objects.all()
    contexto = {'sucursal' : sucursal}
    return render (request,'core/sucursal.html', contexto)

def addsucursal (request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data['direccion']
            messages.success(request, f'sucursal {nombre} agregado con exito')
            
            return redirect('sucursal')
    else:
        form = SucursalForm()

    contexto = {'form' : form}
    return render (request,'core/addsucursal.html', contexto)

def borrarSucursal(request, id):
    sucursal = Sucursal.objects.get(pk=id)
    sucursal.delete()
    messages.success(request, 'Sucursal eliminada con exito')

    return redirect('sucursal')

def pres (request):
    return render (request,'core/pres.html')
def finiquitar_pres (request):
    return render (request,'core/finiquitar_pres.html')
def stock (request):
    stock = Lote.objects.all()
    contexto = {'stock' : stock}

    return render (request,'core/stock.html', contexto)
def addstock (request):
    if request.method == 'POST':
        sucursal = Sucursal.objects.all()[0]
        form = LoteForm(request.POST)
        if form.is_valid():
            guardado = form.save(commit=False)
            guardado.sucursal = sucursal
            guardado.save()
            nombre = form.cleaned_data['tipo']
            messages.success(request, f'Medicamento {nombre} agregado con exito')
            
            return redirect('stock')
    else:
        form = LoteForm()

    contexto = {'form' : form}
    return render (request,'core/addstock.html', contexto)

def borrarStock(request, id):
    lote = Lote.objects.get(pk=id)
    lote.delete()
    messages.success(request, 'Lote eliminado con exito')

    return redirect('stock')

@staff_member_required
def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            nick1 = form.cleaned_data['username']
            messages.success(request, f'Usuario {nick1} creado con exito')
            return redirect('inicio')
    else:
        form = UserForm()

    contexto = { 'form' : form }

    return render(request,'core/registro.html', contexto)