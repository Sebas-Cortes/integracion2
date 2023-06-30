from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from core.forms import LoginForm, LoteForm, SucursalForm, UserForm
from core.models import Lote, Sucursal, Reserva
from django.contrib.admin.views.decorators import staff_member_required
from core.services import get_pres, put_pres, get_res

from core.utils import ActReserva
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
def finiquitar_pres (request, rut):
    lote = Lote.objects.all()
    pres = get_pres(rut)
    estados = []
    cont = []
    boo = bool
    disp = bool
    id = pres[0]['prescripcion']
    if pres == False:
        messages.error(request, 'Error: No hay prescripcion para ese rut')
        return redirect('inicio')
    for i in pres:
        for j in lote:
            if i['medicamento'] == j.tipo and i['cantidad'] <= j.cantidad:
                cont.append(True)
                estados.append({
                    'id' : i['idReceta'],
                    'estado' : True
                })
                break
            else:
                cont.append(False)
        for x in range(len(cont)):
            if cont[x] == True:
                boo = True
                break
            else:
                boo = False
        if boo == False:
            estados.append({
                    'id' : i['idReceta'],
                    'estado' : False
                })
        cont = []
    for z in estados:
        if z['estado'] == False:
            dips = False
            break
        else:
            dips = True

    contexto = {'pres' : pres,
                'rut' : rut,
                'estados' : estados,
                'dips' : dips,
                'id' : id,}

    return render (request,'core/finiquitar_pres.html', contexto)
def stock (request):
    stock = Lote.objects.all()
    contexto = {'stock' : stock}

    return render (request,'core/stock.html', contexto)
def addstock (request):
    if request.method == 'POST':
        reservas = Reserva.objects.all().order_by('fecha')
        sucursal = Sucursal.objects.all()[0]
        form = LoteForm(request.POST)
        if form.is_valid():
            guardado = form.save(commit=False)
            guardado.sucursal = sucursal
            guardado.save()
            nombre = form.cleaned_data['tipo']
            messages.success(request, f'Medicamento {nombre} agregado con exito')
            for r in reservas:
                ActReserva(r.idPres)
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

def consultaPres(request):
    rut1 = request.POST['pres']
    return redirect('finiquitar_pres', rut=rut1)

def descontarPres(request, rut):
    pres = get_pres(rut)
    try:
        for i in pres:
            lote = Lote.objects.get(tipo=i['medicamento'])
            cant = lote.cantidad
            lote.cantidad = cant - i['cantidad']
            lote.save()
        pres2 = put_pres(rut)
        messages.success(request, f'Prescripcion {pres2["rutPaciente"]} finalizada con exito')
    except:
        messages.error(request, 'Error al eliminar la prescripcion intentelo mas tarde')
    return redirect('inicio')

def reservarPres(request, rut):
    pres = get_pres(rut)
    for i in pres:
        idpres = str(i['prescripcion'])
    info = get_res(idpres)
    info = info[0]
    idpres = info['idPrescripcion']
    rut = info['rutPaciente']
    correo = request.POST['correo']
    try:
        Reserva.objects.create(rut=rut, idPres=idpres, email=correo)
        messages.success(request, f'Reserva creada con exito')
    except:
        messages.error(request, 'Error al crear la reserva intentelo mas tarde')
    return redirect('inicio')

def res(request):
    return render(request, 'core/res.html')

def consultarRes(request):
    rut1 = request.POST['pres']
    return redirect('finiquitar_res', rut=rut1)

def finiquitar_res(request, rut):
    lote = Lote.objects.all()
    try:
        res = Reserva.objects.get(rut=rut)
    except Reserva.DoesNotExist:
        messages.error(request, 'No existe reserva para este rut')
        return redirect('inicio')
    pres = get_pres(rut)
    estados = []
    cont = []
    boo = bool
    disp = bool
    if res.estado == False:
        for i in pres:
            for j in lote:
                if i['medicamento'] == j.tipo and i['cantidad'] <= j.cantidad:
                    cont.append(True)
                    estados.append({
                        'id' : i['idReceta'],
                        'estado' : True
                    })
                    break
                else:
                    cont.append(False)
            for x in range(len(cont)):
                if cont[x] == True:
                    boo = True
                    break
                else:
                    boo = False
            if boo == False:
                estados.append({
                        'id' : i['idReceta'],
                        'estado' : False
                    })
            cont = []
        for z in estados:
            if z['estado'] == False:
                dips = False
                break
            else:
                dips = True

        contexto = {'pres' : pres,
                    'rut' : rut,
                    'estados' : estados,
                    'dips' : dips,
                    'res' : True,
                    }
    elif res.estado == True:
        contexto = {'res' : False}
    return render (request,'core/finiquitar_res.html', contexto)

def descontarRes(request, rut):
    pres = get_pres(rut)
    res = Reserva.objects.get(rut=rut)
    res.delete()
    try:
        pres2 = put_pres(rut)
        messages.success(request, f'Prescripcion {pres2["rutPaciente"]} finalizada con exito')
    except:
        messages.error(request, 'Error al eliminar la prescripcion intentelo mas tarde')
    return redirect('inicio')
