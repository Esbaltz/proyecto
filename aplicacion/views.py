from django.shortcuts import render
from .models import Libro
from .forms import Agregar_libroForm
# Create your views here.

# Vistas principales 
def index(request):

    libro = Libro.objects.all()
    data = {
        'libro': libro
    }
    return render(request, 'aplicacion/index.html', data)

def tienda(request):
    
    libro = Libro.objects.all()
    data = {
        'libro': libro
    }
    return render(request, 'aplicacion/tienda.html', data)

def gral_libro(request):
    return render(request, 'aplicacion/pagina_general_libro.html')

def inf_pago(request):
    return render(request, 'aplicacion/inf_pago.html')

def carrito(request):
    return render(request, 'aplicacion/pagina_carrito_general.html')

def domicilio(request):
    return render(request, 'aplicacion/pagina_domicilio_y_pagar.html')

#Vistas de usuario
def usuario(request):
    return render(request, 'aplicacion/usuario/user.html')

#Vistas de sesión
def c_contra(request):
    return render(request, 'aplicacion/paginas_inicio_secion/Cambio_de_contraseña.html')

def ini_sesion(request):
    return render(request, 'aplicacion/paginas_inicio_secion/Inicio_secion.html')

def reg_user(request):
    return render(request, 'aplicacion/paginas_inicio_secion/Registro_usuario.html')

#Vistas de las categorias de libros
def biografia(request):
    libro = Libro.objects.all()
    data = {
        'libro': libro
    }
    return render(request, 'aplicacion/libros_categorias/biografia.html', data)

def historia(request):
    libro = Libro.objects.all()
    data = {
        'libro': libro
    }
    return render(request, 'aplicacion/libros_categorias/historia.html', data)

def misterio(request):
    libro = Libro.objects.all()
    data = {
        'libro': libro
    }
    return render(request, 'aplicacion/libros_categorias/misterio.html', data)

def sci_fi(request):
    libro = Libro.objects.all()
    data = {
        'libro': libro
    }
    return render(request, 'aplicacion/libros_categorias/sci_fi.html', data)

def terror(request):
    libro = Libro.objects.all()
    data = {
        'libro': libro
    }
    return render(request, 'aplicacion/libros_categorias/terror.html', data)

#Vistas admin
def agregar(request):
    mensaje = ""
    if request.method == 'POST':
        formulario = Agregar_libroForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            mensaje = "Libro agregado con éxito"
            # Puedes añadir más lógica aquí después de guardar el formulario
            #hacer en el form con el widyet
        else:
            mensaje = "Ha ocurrido un error. Verifica los datos ingresados."
            # Si el formulario no es válido, puedes manejar los errores aquí
    formulario = Agregar_libroForm()
        # Puedes enviar más datos al contexto si es necesario
    return render(request, 'aplicacion/imenu-w/agregar_producto.html', {'form': formulario, 'mensaje': mensaje})

def buscar(request):
    return render(request, 'aplicacion/imenu-w/buscar_producto.html')

def crear(request):
    return render(request, 'aplicacion/imenu-w/crear_cuenta.html')

def eliminar(request):
    return render(request, 'aplicacion/imenu-w/eliminar_producto.html')

def modificar(request):
    return render(request, 'aplicacion/imenu-w/modificar_producto.html')

def pedidos(request):
    return render(request, 'aplicacion/imenu-w/pedidos.html')

def usuario_gnral(request):
    return render(request, 'aplicacion/imenu-w/usuario_gnral.html')

def usuarios(request):
    return render(request, 'aplicacion/imenu-w/usuarios.html')
