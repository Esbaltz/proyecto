from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
#from .models import Product
from django import forms
from .models import Libro
from django.http import JsonResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

"""
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group mb-0 col-md-6'),
                Column('price', css_class='form-group mb-0 col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('stock', css_class='form-group mb-0 col-md-6'),
                Column('description', css_class='form-group mb-0 col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('image', css_class='form-group mb-0 col-md-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Agregar Producto', css_class='btn btn-primary')
        )
        # Add custom classes to fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
"""

#def index(request):
 #   products = Product.objects.all()
 #   return render(request, 'pages/index.html', {'products': products})
"""""
def delete_product(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return redirect('index')
    return JsonResponse({'error': 'Invalid request method'}, status=400)
    
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    
    products = Product.objects.all()
    return render(request, 'pages/index.html', {'products': products, 'form': form})
"""
class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class Libro_agregarForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['isbn', 'nombre','nombre_autor','tipo', 'precio','subtipo', 'best_seler','foto']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['isbn', 'nombre', 'nombre_autor', 'foto', 'precio', 'best_seler', 'tipo', 'subtipo']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre del libro debe tener al menos 3 caracteres.')
        return nombre

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if len(isbn) < 10 or len(isbn) > 13:
            raise forms.ValidationError('El ISBN debe tener entre 10 y 13 caracteres.')
        return isbn

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo.')
        return precio

    def clean_nombre_autor(self):
        nombre_autor = self.cleaned_data.get('nombre_autor')
        if len(nombre_autor) < 3:
            raise forms.ValidationError('El nombre del autor debe se mayor a 3 cáracteres.')
        # Aquí podrías agregar otras validaciones según tus requisitos
        return nombre_autor

    # Añade más métodos clean_ según sea necesario para otros campos

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        # Puedes agregar validaciones personalizadas para la foto si lo necesitas
        return foto

    def clean_best_seler(self):
        best_seler = self.cleaned_data.get('best_seler')
        # Puedes agregar validaciones personalizadas para best_seler si lo necesitas
        return best_seler

    def clean_tipo(self):
        tipo = self.cleaned_data.get('tipo')
        # Puedes agregar validaciones personalizadas para tipo si lo necesitas
        return tipo

    def clean_subtipo(self):
        subtipo = self.cleaned_data.get('subtipo')
        # Puedes agregar validaciones personalizadas para subtipo si lo necesitas
        return subtipo