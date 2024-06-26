from django import forms
from .models import Libro

class Agregar_libroForm(forms.ModelForm):

    class Meta:

        model = Libro
        fields =['nombre', 'isbn', 'nombre_autor', 'subtipo', 'precio', 'foto']