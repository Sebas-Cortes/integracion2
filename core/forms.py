from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'name': 'user','placeholder':'Nombre de usuario'}))
    password = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'name': 'pass','placeholder':'Contraseña'}))