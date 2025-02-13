# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario



class RegistroForm(UserCreationForm):
    genero = forms.ChoiceField(choices=Usuario.GENERO_CHOICES, required=False)
    telefone = forms.CharField(max_length=15, required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'genero', 'telefone', 'password1', 'password2']
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
