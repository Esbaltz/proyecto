from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrito, Libro, Usuario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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
    usuario = request.user
    if not isinstance(usuario, Usuario):
        # Manejar el caso cuando `request.user` no es un Usuario válido
        # Puedes redirigir a otra página o mostrar un mensaje de error
        return HttpResponse("Usuario no válido")

    carrito_usuario = Carrito.objects.filter(comprador_carrito=usuario)
    total_carrito = sum(item.libro.precio * item.cantidad for item in carrito_usuario)

    data = {
        'carrito': carrito_usuario,
        'total_carrito': total_carrito,
    }
    return render(request, 'aplicacion/pagina_carrito_general.html', data)

def agregar_al_carrito(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    usuario = request.user  # Obtener el usuario actual, ajusta según tu autenticación

    # Verificar si ya existe el libro en el carrito del usuario
    carrito, created = Carrito.objects.get_or_create(comprador_carrito=usuario, libro=libro)

    if not created:
        carrito.cantidad += 1
        carrito.save()

    return redirect('carrito')  

def eliminar_del_carrito(request, carrito_id):
    carrito = get_object_or_404(Carrito, id=carrito_id)
    carrito.delete()
    return redirect('carrito') 

def domicilio(request):
    return render(request, 'aplicacion/pagina_domicilio_y_pagar.html')

#Vistas de usuario
def usuario(request):
    return render(request, 'aplicacion/usuario/user.html')

#Vistas de sesión
def c_contra(request):
    return render(request, 'aplicacion/paginas_inicio_secion/Cambio_de_contraseña.html')

def ini_sesion(request):
    if request.method == 'POST':
        nombre_cuenta = request.POST['nombreCuenta']
        contraseña = request.POST['password']
        user = authenticate(request, username=nombre_cuenta, password=contraseña)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nombre de cuenta o contraseña incorrectos.')
    return render(request, 'aplicacion/paginas_inicio_secion/Inicio_secion.html')

def reg_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}!')
            return redirect('ini_sesion')
    else:
        form = UserCreationForm()
    return render(request, 'aplicacion/paginas_inicio_secion/Registro_usuario.html', {'form': form})

# Vistas de las categorías de libros

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
    return render(request, 'aplicacion/imenu-w/agregar_producto.html')

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
