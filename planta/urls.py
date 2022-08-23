#Creacion de vistas para app
from django.urls import URLPattern, path
from . import views

app_name='planta'

urlpatterns =[
    path('', views.index, name = "index"),
    path('trabajador', views.listarTrabajador, name='trabajador'),
    path('aggTrabajador/',views.agregarTrabajador,name='aggTrabajador'),
    path('guardarTrabajador/',views.guardarTarabajador,name='guardarTrabajador'),
    
]