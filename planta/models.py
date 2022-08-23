
from datetime import date
from django.db import models


# Create your models here.

class Trabajador(models.Model):
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fechaNacimiento = models.DateField()
    correo = models.EmailField(max_length=250,null=True,blank=True)

    def edad(self):
        año = date.today()
        fecha = self.fechaNacimiento
        edad = fecha.year-año.year
        return f'{edad}'

    def nombreCompleto(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

    

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    desc = models.CharField(max_length=254,null=True,blank=True)

    
    def __str__(self) -> str:
        return f'{self.nombre} '

class Productos(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    ficha = models.TextField()
    costo = models.IntegerField()
    categoria = models.ForeignKey(Categoria ,on_delete=models.DO_NOTHING)
    COLOR=(
        ('r','Rojo'),
        ('v','Verde'),
        ('a','Azul')
    )
    color=models.CharField(max_length=200,choices=COLOR,default='r')
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.categoria}'

class Produccion(models.Model):
    trabajador = models.ForeignKey(Trabajador,on_delete=models.DO_NOTHING)
    productos = models.ForeignKey(Productos,on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField()

    
    def __str__(self) -> str:
        return f'{self.trabajador} {self.productos}'
