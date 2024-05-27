#URLS APLICACION
from django.urls import path, include
from .views import index, tienda, gral_libro

#URLS DE SITIO
urlpatterns = [
    path('', index, name='index'),
    path('tienda/', tienda, name='tienda'),
    path('pagina_general_libro/', gral_libro, name='libro'),
]