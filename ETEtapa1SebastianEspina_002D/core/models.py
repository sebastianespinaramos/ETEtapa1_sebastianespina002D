from django.db import models

# Create your models here.
class usuario(models.Model):
    NomCompleto=models.CharField(max_length=30, verbose_name='Nombre del Usuario')
    email=models.CharField(max_length=50, primary_key=True,verbose_name='Correo del usuario')
    direccion=models.CharField(max_length=40 ,verbose_name='Dirección del usuario')
    contraseña=models.CharField( max_length=10,verbose_name='Contraseña del usuario')
    def __str__(self):
        return self.email

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre  

