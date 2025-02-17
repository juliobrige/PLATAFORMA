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
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) > 8:
            raise ValidationError("A senha deve ter no máximo 8 caracteres.")
        return password1
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
