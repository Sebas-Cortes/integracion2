from django.shortcuts import render
from django.contrib.auth.views import LoginView

from core.forms import LoginForm

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
    return render (request,'core/stock.html')
def addstock (request):
    return render (request,'core/addstock.html')