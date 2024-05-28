#URLS APLICACION
from django.urls import path, include
from .views import index, tienda, gral_libro, inf_pago, carrito, domicilio

#URLS DE SITIO
urlpatterns = [
    path('', index, name='index'),
    path('tienda/', tienda, name='tienda'),
    path('pagina_general_libro/', gral_libro, name='libro'),
    path('inf_pago/', inf_pago, name='inf_pago'),
    path('pagina_carrito_general/', carrito, name='carrito'),
    path('pagina_domicilio_y_pagar/', domicilio, name='domicilio'),
]