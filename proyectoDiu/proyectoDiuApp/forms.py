from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    apellido_paterno = forms.CharField(max_length=30, required=False)
    apellido_materno = forms.CharField(max_length=30, required=False)
    fecha_nacimiento = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', )
        
        
        
