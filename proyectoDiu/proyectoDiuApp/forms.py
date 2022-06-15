from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cita
from django.forms import ModelForm, Widget

class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    apellido_paterno = forms.CharField(max_length=30, required=False)
    apellido_materno = forms.CharField(max_length=30, required=False)
    fecha_nacimiento = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', )



class CitaForm(ModelForm):
    nombre = forms.TextInput(attrs={'class':'form-control'})
    apellido1 = forms.TextInput(attrs={'class':'form-control'})
    apellido2 =forms.TextInput(attrs={'class':'form-control'})
    CURP = forms.TextInput(attrs={'class':'form-control'})
    direccion = forms.TextInput(attrs={'class':'form-control'})
    cita_fecha  =forms.DateTimeInput(attrs={
            'class': 'datepicker'
        })  
    
    class Meta():
        # fields = '__all__'
        model = Cita
        verbose_name_plural='citas'
        widgets ={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido1':forms.TextInput(attrs={'class':'form-control'}),
            'apellido2':forms.TextInput(attrs={'class':'form-control'}),
            'CURP':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self):
        self.cita_fecha.input_formats = ['%d/%m/%Y']
        self.cita_fecha.widget = forms.DateTimeInput(attrs={
            'class': 'datepicker'
        })  

    class Meta:
        fields = '__all__'

    def __str__(self):
        return self.nombre
 
        
        
