from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrito, Libro, Usuario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm, Libro_agregarForm, LibroForm, LibroFormMod
from django.contrib.auth import logout
from django.contrib.auth.models import User
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

def detallelibro(request, isbn):
    return render(request, 'aplicacion/detallelibro.html')

def inf_pago(request):
    return render(request, 'aplicacion/inf_pago.html')
@login_required
def carrito(request):
    usuario =  request.user.id
    carrito_items = Carrito.objects.filter(comprador_carrito=usuario)
    total = sum(item.libro.precio * item.cantidad for item in carrito_items)
    return render(request, 'aplicacion/pagina_carrito_general.html', {'carrito_items': carrito_items, 'total': total})

def agregar_al_carrito(request, isbn):
    libro = get_object_or_404(Libro, isbn=isbn)
    usuario = request.user  # Obtener el usuario actual

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
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir a una página después del inicio de sesión exitoso
                return redirect('index')  # Ajusta 'dashboard' según tu configuración de URLs
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'aplicacion/paginas_inicio_secion/Inicio_secion.html', {'form': form})

def salir(request):
    logout(request)
    messages.info(request,'Sesión Cerrada')
    return redirect(to="index")

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
    exito = False  # Variable para controlar si mostrar el mensaje de éxito
    
    if request.method == 'POST':
        form = LibroForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            exito = True  # Cambia el estado de éxito a True después de guardar el libro correctamente
    else:
        form = LibroForm()

    data = {
        'form': form,
        'exito': exito,  # Pasar la variable exito al contexto de la plantilla
    }
    return render(request, 'aplicacion/imenu-w/agregar_producto.html', data)

def buscar(request):
    libros = Libro.objects.all()

    data={
        'libros': libros
    }
    return render(request, 'aplicacion/imenu-w/buscar_producto.html', data)

def crear(request):
    return render(request, 'aplicacion/imenu-w/crear_cuenta.html')

def eliminar(request, isbn):
    libro = get_object_or_404(Libro, isbn=isbn)
    libro.delete()
    return redirect(to="buscar")

def modificar(request, isbn):
    libro = get_object_or_404(Libro, isbn=isbn)
    exito = False

    if request.method == 'POST':
        formulario = LibroFormMod(request.POST, request.FILES, instance=libro)
        if formulario.is_valid():
            formulario.save()
            exito = True  # Cambia el estado de éxito a True después de guardar los cambios correctamente
    else:
        formulario = LibroFormMod(instance=libro)
        # No permitir modificar el campo isbn en el formulario
        formulario.fields['isbn'].disabled = True

    data = {
        'form': formulario,
        'exito': exito,  # Pasar la variable exito al contexto de la plantilla
    }
    return render(request, 'aplicacion/imenu-w/modificar_producto.html', data)

def libro(request):
    return render(request, 'aplicacion/tienda.html')

def pedidos(request):
    return render(request, 'aplicacion/imenu-w/pedidos.html')

def usuario_gnral(request):
    return render(request, 'aplicacion/imenu-w/usuario_gnral.html')

def usuarios(request):
    return render(request, 'aplicacion/imenu-w/usuarios.html')
