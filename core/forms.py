from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from core.models import Lote, Sucursal


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'name': 'user','placeholder':'Nombre de usuario'}))
    password = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'name': 'pass','placeholder':'Contraseña'}))
    
class LoteForm(forms.ModelForm):
    class Meta:
        model = Lote
        fields = ['tipo', 'cantidad']
        helps_texts = {k: "" for k in fields}
        labels = {
            'tipo' : 'Nombre del medicamento',
            'cantidad' : 'Cantidad',
        }
        widgets = {
            'tipo' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Nombre del medicamento',
            }),
            'cantidad' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Cantidad',
            }),
        }

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['direccion', 'comuna', 'region']
        help_texts = {k: "" for k in fields}
        labels = {
            'direccion' : 'Direccion',
            'comuna' : 'Comuna',
            'region' : 'Region',
        }
        widgets = {
            'direccion' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Direccion',
            }),
            'comuna' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Comuna',
            }),
            'region' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Region'
            })
        }
