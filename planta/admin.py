from django.contrib import admin
from .models import Trabajador,Categoria,Produccion,Productos
# Register your models here.

admin.site.register(Trabajador)
admin.site.register(Categoria)
admin.site.register(Productos)
admin.site.register(Produccion)