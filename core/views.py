from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from core.forms import LoginForm, LoteForm
from core.models import Lote, Sucursal

# Create your views here.
def login(request):
    return render(request, 'core/login.html')

class CustomLoginView(LoginView):
    template_name = "core/login.html"
    form_class = LoginForm

def inicio (request):
    return render (request,'core/inicio.html')
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
        sucursal = Sucursal.objects.get(pk=1)
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