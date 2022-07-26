from django import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'planta/index.html')

def saludar(request):
    return HttpResponse("Hola mundo")

def despedir(request):
    return HttpResponse("Adios prro <a href='http://127.0.0.1:8000/planta/saludar/'>Click aqui</a>")

def saludoEspecial(request,nombre):
    return HttpResponse(f"Hola {nombre}")

def multiplo(request,num,num2):
    return HttpResponse(f"Hola tu resultado es {num*num2}")

def loginFormulario(request):
    return render(request,'planta/login/login-form.html')

def login(request):
    u=request.POST['usuario']
    c=request.POST['clave']

    if u=='felipe' and c=='123':
        return HttpResponse('Bienvenido')
    else:
        return HttpResponse('Usuario o contraseña incorrectos!!')

def sumaFormulario(request):
    return render(request,'planta/suma/suma.html')

def suma(request):
    n1=request.POST['numero1']
    n2=request.POST['numero2']

    r=int(n1)+int(n2)

    return HttpResponse (f'La suma de {n1} y {n2} es {r}')