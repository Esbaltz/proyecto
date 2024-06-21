"""
URL configuration for sitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aplicacion import views as views

urlpatterns = [
    path('admin/', admin.site.urls),


    
    #Páginas principales
    path('', views.index, name='index'),
    path('tienda/', views.tienda, name='tienda'),
    path('pagina_general_libro/', views.gral_libro, name='libro'),
    path('inf_pago/', views.inf_pago, name='inf_pago'),
    path('pagina_carrito_general/', views.carrito, name='carrito'),
    path('pagina_domicilio_y_pagar/', views.domicilio, name='domicilio'),

    #Páginas usuario
    path('user/', views.usuario, name='usuario'),

    #Paginas inicio de sesión
    path('Cambio_de_contraseña/', views.c_contra, name='c_contra'),
    path('Inicio_secion/', views.ini_sesion, name='ini_sesion'),
    path('Registro_usuario/', views.reg_user, name='reg_user'),

    #Páginas categorias de libros
    path('biografia/', views.biografia, name='biografia'),
    path('historia/', views.historia, name='historia'),
    path('misterio/', views.misterio, name='misterio'),
    path('sci_fi/', views.sci_fi, name='sci_fi'),
    path('terror/', views.terror, name='terror'),

    #Admin
    path('agregar/', views.agregar, name='agregar'),
    path('buscar/', views.buscar, name='buscar'),
    path('crear/', views.crear, name='crear'),
    path('eliminar/', views.eliminar, name='eliminar'),
    path('modificar/', views.modificar, name='modificar'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('usuario_gnral/', views.usuario_gnral, name='usuario_gnral'),
    path('usuarios/', views.usuarios, name='usuarios'),
]

