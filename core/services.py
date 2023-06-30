import requests

def get_pres(rut):
    url = 'http://127.0.0.1:8080/api/pres/' + rut
    r = requests.get(url)
    if r == None:
        pres = False
        return pres
    else: 
        pres = r.json()
        pres_list = []
        for i in range(len(pres)):
            pres_list.append(pres[i])
        return pres


def put_pres(rut):
    url = 'http://127.0.0.1:8080/api/putPres/' + rut
    data = {
            'rutPaciente' : rut,
            'estado' : False
        }
    r = requests.put(url, json = data)

    if r.status_code == 200:
        print('Solicitud exitosa')
        
        return r.json()
    else:
        print('Error en la solicitud:', r.status_code)

def get_res(id):
    url = 'http://127.0.0.1:8080/api/getPres/' + str(id)
    r = requests.get(url)
    pres = r.json()
    return pres