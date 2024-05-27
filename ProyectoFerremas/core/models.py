from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Marca(models.Model):
    descripcion = models.CharField(max_length=10)

    def __str__(self):
        return self.descripcion

    

class Genero(models.Model):
    tipo= models.CharField(max_length=10)
    
    def __str__(self):
        return self.tipo

class TipoEmpleado(models.Model):
    tipo=models.CharField(max_length=15)

    def __str__(self):
        return self.tipo


class CategoriaProducto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    categoria = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.categoria
    
class Producto(models.Model):
    
    nombre = models.CharField(max_length=64, null = False)
    categoria = models.ForeignKey(CategoriaProducto, on_delete = models.CASCADE)
    descripcion = models.TextField()
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(null=True, upload_to='productos/')

    def __str__(self):
        return self.nombre

    


#class Producto(models.Model):
#    Nombre = models.CharField(max_length=50)
#    tipo = models.ForeignKey(TipoHerramienta, on_delete=models.CASCADE)
#    descripcion = models.TextField()  
#    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
#    imagen = models.ImageField(upload_to="noticias", null=True)
#    precio = models.IntegerField

#    def __str__(self):
#        return self.Nombre


class Empleado(models.Model):
    rut= models.CharField (max_length=50)
    Nombre = models.CharField(max_length=50)
    apellidoP=models.CharField(max_length=50)
    apellidoM=models.CharField(max_length=50)
    puesto = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Nombre

#Carrito

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)

    def str(self):
        return f"{self.usuario} - {self.creado_en}"

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def precio_total(self):
        return self.cantidad * self.precio
    

class Boleta(models.Model):
    total = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

class DetalleBoleta(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

