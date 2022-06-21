from pickle import NONE
from tabnanny import verbose
from turtle import title
from unicodedata import category
from django.db import models 
from django import forms
from django.forms import ModelForm, Widget
from django.contrib.auth.models import User


# Create your models here.
class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, related_name='created_by',on_delete=models.CASCADE,default=None)
    nombre = models.CharField(max_length=255)
    apellido1 = models.CharField(max_length=255)
    apellido2 = models.CharField(max_length=255)
    CURP = models.CharField(max_length=10)
    direccion = models.CharField(max_length=650)
    ine = models.FileField(upload_to ='documentos/identificacion')
    passaporte_anterior = models.FileField(upload_to ='documentos/pasaporte',blank=True)
    matricula_anterior = models.FileField(upload_to ='documentos/matricula',blank=True)
    identifacion_padre = models.FileField(upload_to ='documentos/padres',blank=True)
    cita_fecha = models.DateField( blank=True) #recuerda cambiar ese dato
    pago = models.CharField(max_length=255, default="")
     
    

#---------------Creo los formularios
