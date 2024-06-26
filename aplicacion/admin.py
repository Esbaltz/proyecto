from django.contrib import admin

# Register your models here.

from .models import Libro, Usuario, Carrito, Pedido, DetallePedido

models = [Libro, Usuario, Carrito, Pedido, DetallePedido]
for model in models:
    admin.site.register(model)