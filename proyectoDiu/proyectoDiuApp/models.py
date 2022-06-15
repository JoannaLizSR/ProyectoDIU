from datetime import datetime
from django.db import models
from tabnanny import verbose
from turtle import title
from unicodedata import category
from django import forms
from django.forms import ModelForm, Widget



# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaRegistro = models.DateField(default= datetime.now())

    def __str__(self):
        return f'email: {self.email} fechaRegsitro: {self.fechaRegistro}'

        
class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
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
