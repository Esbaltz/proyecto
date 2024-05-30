#URLS APLICACION
from django.urls import path, include
from .views import index, tienda, gral_libro, inf_pago, carrito, domicilio, usuario, c_contra, ini_sesion, reg_user, biografia, historia, misterio, sci_fi, terror, agregar, buscar, crear, eliminar, modificar, pedidos, usuario_gnral, usuarios

#URLS DE SITIO
urlpatterns = [
    #Páginas principales
    path('', index, name='index'),
    path('tienda/', tienda, name='tienda'),
    path('pagina_general_libro/', gral_libro, name='libro'),
    path('inf_pago/', inf_pago, name='inf_pago'),
    path('pagina_carrito_general/', carrito, name='carrito'),
    path('pagina_domicilio_y_pagar/', domicilio, name='domicilio'),

    #Páginas usuario
    path('user/', usuario, name='usuario'),

    #Paginas inicio de sesión
    path('Cambio_de_contraseña/', c_contra, name='c_contra'),
    path('Inicio_secion/', ini_sesion, name='ini_sesion'),
    path('Registro_usuario/', reg_user, name='reg_user'),

    #Páginas categorias de libros
    path('biografia/', biografia, name='biografia'),
    path('historia/', historia, name='historia'),
    path('misterio/', misterio, name='misterio'),
    path('sci_fi/', sci_fi, name='sci_fi'),
    path('terror/', terror, name='terror'),

    #Admin
    path('agregar/', agregar, name='agregar'),
    path('buscar/', buscar, name='buscar'),
    path('crear/', crear, name='crear'),
    path('eliminar/', eliminar, name='eliminar'),
    path('modificar/', modificar, name='modificar'),
    path('pedidos/', pedidos, name='pedidos'),
    path('usuario_gnral/', usuario_gnral, name='usuario_gnral'),
    path('usuarios/', usuarios, name='usuarios'),
]