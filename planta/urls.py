#Creacion de vistas para app
from django.urls import URLPattern, path
from . import views

app_name='planta'

urlpatterns =[
    path('', views.index, name = "index"),
    
]