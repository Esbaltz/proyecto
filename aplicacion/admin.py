from django.contrib import admin

# Register your models here.

from .models import Libro, Usuario, Carrito, Pedido, Detalle_pedido

models = [Libro, Usuario, Carrito, Pedido, Detalle_pedido]
for model in models:
    admin.site.register(model)