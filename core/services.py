import requests

def get_pres(rut):
    url = 'http://127.0.0.1:8080/api/pres/' + rut
    r = requests.get(url)
    pres = r.json()
    pres_list = []
    for i in range(len(pres)):
        pres_list.append(pres[i])
    return pres
