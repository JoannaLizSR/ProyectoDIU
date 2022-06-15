from datetime import datetime
from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaRegistro = models.DateField(default= datetime.now())

    def __str__(self):
        return f'email: {self.email} fechaRegsitro: {self.fechaRegistro}'
