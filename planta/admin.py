from django.contrib import admin
from .models import Trabajador,Categoria,Produccion,Productos
# Register your models here.

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display= ('id','cedula','nombre','apellido','correo','nombreCompleto')
    search_fields=['nombre','id','cedula']


@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display= ('nombre', 'ficha','costo', 'categoria','color','descriptionCategoria' )
    list_filter=['categoria']
    search_fields=['nombre','categoria__nombre']
    #list_editable=['color']

    def descriptionCategoria(self,obj):
        return obj.categoria.desc

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('id','nombre', 'desc', )


@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display=('id','trabajador', 'productos', 'cantidad', 'fecha', )





