from django.db import models
from .listas import TIPO_GENERO,SUBTIPO_GENERO,TIPO_ESTADO
# Create your models here.
from django.core.validators import MinValueValidator
# Create your models here.
class Libro(models.Model):
    #no se si dejar el isbn como clave primaria o ponerle un id para diferenciarlos
    isbn=models.CharField(max_length=10, primary_key=True, null=False)
    nombre=models.CharField(max_length=50, null=False)
    nombre=models.CharField(max_length=50, null=False)#falta el autor en el html
    foto=models.ImageField("Imagen",upload_to='libros',null=True)
    precio=models.IntegerField(validators=[MinValueValidator(0)])
    best_seler= models.BooleanField()#Falta agregar en el html el boton deslizante de si o no en el html

    tipo=models.CharField(max_length=30, choices=TIPO_GENERO)
    subtipo=models.CharField(max_length=40, choices=SUBTIPO_GENERO, default='Sin subtipo')
    def __str__(self):
        return self.nombre
        #return f"nombre {self.nombre} precio: {self.precio} "
    
class Usuario(models.Model):
    id=models.AutoField(primary_key=True)
    direccion=models.CharField(max_length=60, null=False)#poner un minimo de 3 como en el js
    correo=models.CharField(max_length=100, null=False)
    contraseña=models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    comprador_carrito=models.OneToOneField(Usuario, on_delete=models.PROTECT)
    libro=models.ForeignKey(Libro, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    def __str__(self):
        return self.cantidad

class Pedido(models.Model):
    numero_pedido=models.AutoField(primary_key=True)
    comprador_carrito=models.ForeignKey(Usuario, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    #agregar fecha
    fecha_pedido = models.DateField()
    #agregar estado
    estado_pedido=models.CharField(max_length=40, choices=TIPO_ESTADO)#NO ESTOY SEGURO SI VA ACA

    def __str__(self):
        return self.numero_pedido

class Detalle_pedido(models.Model):
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    pedido =models.ForeignKey(Pedido, on_delete=models.PROTECT)
    producto =models.ForeignKey(Libro, on_delete=models.PROTECT)
    cantidad_un_producto = models.PositiveIntegerField()

    def __str__(self):
        return self.creado_fecha

#no se si dejar la entidad oferta, pero como esta en la pagina, los determinados libros con descuento estan separados de los normales en la pagina general
#class libro_oferta(models.Model):
   # d#escuento = models.DecimalField(max_digits=10, decimal_places=2)
   # def __str__(self):
    #    return self.libro
    


#se reutiliza el detalle del pedido para TENER LA INFORMACION DEL HISTORICO DE LAS COMPRAS QUE VE EL ADMIN Y EL MISMO USUARIO
#o ocupar lo que me ayudo chat gpt y hacerlo de la forma de abajo :v



    

#Hacer el boton de tipo targeta reciclando el boton del domicilio para los 4 tipos de targeta de forma manual tipo boton deslizable

#tambien falta hacer los def para que las clases devuelvan la infrormacion, pero al final XD

#Debemos realizar el logo de nuevo que contenga: .¿(despues XD)
