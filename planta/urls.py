#Creacion de vistas para app
from django.urls import URLPattern, path
from . import views

app_name='planta'

urlpatterns =[
    path('', views.index, name = "index"),
    path('saludar/', views.saludar, name = "saludar"),
    path('adios/', views.despedir, name = "despedir"),
    path('saludo-especial/<str:nombre>', views.saludoEspecial, name = "especial"),
    path('numero/<int:num>/<int:num2>', views.multiplo, name = "multiplo"),
    path('login-formulario', views.loginFormulario, name = "loginf"),
    path('loginV', views.login, name = "login"),
    path('suma-formulario',views.sumaFormulario,name='sumaF'),
    path('suma',views.suma,name='suma')
]