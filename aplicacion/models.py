from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .listas import TIPO_GENERO, SUBTIPO_LIBRO
# Create your models here.
class Libro(models.Model):
    #no se si dejar el isbn como clave primaria o ponerle un id para diferenciarlos
    isbn=models.CharField(max_length=10, primary_key=True, null=False)
    nombre=models.CharField(max_length=50, null=False)
    foto=models.ImageField("Imagen",upload_to='personas',null=True)
    precio=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(300)])
    tipo=models.CharField(max_length=30, choices=TIPO_GENERO)
    subtipo=models.CharField(max_length=20, choices=SUBTIPO_LIBRO, default='Sin subtipo')
    es_best_seler = models.BooleanField(default=True)

    def __str__(self):
        return f"nombre {self.nombre} precio: {self.precio} "
    
class Usuario(models.Model):
    id=models.CharField(max_length=10, primary_key=True, null=False)
    nombre=models.CharField(max_length=50, null=False)
    correo=models.CharField(max_length=100, null=False)
    contraseña=models.CharField(max_length=100, null=False)

class Carrito(models.Model):

    comprador_carrito=models.ForeignKey(Usuario, on_delete=models.PROTECT)
    libro=models.ForeignKey(Libro, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()


class Pedido(models.Model):
    numero_pedido=models.CharField(max_length=10, primary_key=True, null=False)
    comprador_carrito=models.ForeignKey(Usuario, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class Detalle_pedido(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    pedido =models.ForeignKey(Pedido, on_delete=models.PROTECT)
    producto =models.ForeignKey(Libro, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    creado_fecha = models.DateTimeField(auto_now_add=True)

#no se si dejar la entidad oferta, pero como esta en la pagina, los determinados libros con descuento estan separados de los normales en la pagina general
class libro_oferta(models.Model):
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    libro=models.ForeignKey(Libro, on_delete=models.PROTECT)
    


#no se si agregar la fecha en el detalle del pedido y reutilizarlo como historial de compra
#o ocupar lo que me ayudo chat gpt y hacerlo de la forma de abajo :v