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

