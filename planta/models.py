from operator import truediv
from django.db import models

# Create your models here.

class trabajador(models.Model):
    cedula = models.IntegerField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellido= models.CharField(max_length=200)
    correo=models.EmailField(max_length=250,null=True,blank=True)