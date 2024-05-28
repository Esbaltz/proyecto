from django.shortcuts import render

# Create your views here.
def index(request):
    print(request)
    return render(request, 'aplicacion/index.html')

def tienda(request):
    print(request)
    return render(request, 'aplicacion/tienda.html')

def gral_libro(request):
    return render(request, 'aplicacion/pagina_general_libro.html')

def inf_pago(request):
    return render(request, 'aplicacion/inf_pago.html')

def carrito(request):
    return render(request, 'aplicacion/pagina_carrito_general.html')

def domicilio(request):
    return render(request, 'aplicacion/pagina_domicilio_y_pagar.html')


