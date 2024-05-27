from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Marca)
admin.site.register(Genero)
admin.site.register(TipoEmpleado)
admin.site.register(Producto)
admin.site.register(Empleado)
admin.site.register(CategoriaProducto)