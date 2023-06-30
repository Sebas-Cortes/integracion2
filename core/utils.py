from core.services import get_res
from core.models import Lote, Reserva
from django.core.mail import send_mail

def enviarCorreo(asunto, mensaje, destinatario):
    send_mail(asunto, mensaje, 'sebastian21384@gmail.com', [destinatario])

def ActReserva(id):
    data = get_res(id)
    recetas = data[0]['recetas']
    lote = Lote.objects.all()
    reserva = Reserva.objects.get(idPres = id)
    booleanos = []
    estado = False

    for receta in recetas:
        med = receta['medicamento']
        cant = receta['cantidad']
        for l in lote:
            if med.upper() == l.tipo.upper():
                if cant <= l.cantidad:
                    booleanos.append({
                        'medicamento' : med,
                        'cantidad' : cant,
                        'bool' : True,
                    })
                else:
                    booleanos.append({
                        'medicamento' : med,
                        'cantidad' : cant,
                        'bool' : False,
                    })
                    print(f'Medicamento {med} insuficiente')
                
    for bool in booleanos:
        if bool['bool'] == False:
            estado = False
            break
        else: 
            estado = True
    
    for bool in booleanos:
        if estado :
            l = Lote.objects.get(tipo=bool['medicamento'])
            l.cantidad = l.cantidad - bool['cantidad']
            l.save()
            reserva.estado = False
            reserva.save()
            print('Reserva activada y descontada con exito')
        else:
            break
    if estado:
        enviarCorreo('Reserva medicamentos', f'Estimado/a: Sus medicamentos de la prescripcion Nro: {id} estan listos para su retiro', reserva.email)