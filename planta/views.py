from django import http
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from urllib import request

#Mensaje tipo cookie temporales
from django.contrib import messages

#Gestion de errores de bases de datos
from django.db import IntegrityError
from .models import Trabajador,Categoria,Produccion,Productos



# Create your views here.
def index(request):
    return render(request, 'planta/index.html')

def listarTrabajador(request):
    q=Trabajador.objects.all()
    context = {"datos": q}
    return render(request, 'planta/trabajador/trabajador.html',context)

def agregarTrabajador(request):
    return render(request, 'planta/trabajador/aggTrabajador.html')

def guardarTarabajador(request):
    try:
        if request.method=='POST':
            q = Trabajador(
                cedula = request.POST["cedula"],
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                fechaNacimiento = request.POST["fechaNacimiento"],
                correo = request.POST["correo"]
            )
            q.save()
            messages.success(request, "Trabajadro guardado correctamente!!")
        else:
            messages.warning(request, "Usted no ha enviado datos!!")
    except Exception as e:
        messages.error(request, f"Error: {e}")
        
    return redirect('planta:trabajador')