from django.db import models

# Create your models here.
class Usuario:
    id=models.CharField(max_length=12, primary_key=True, null=False)
    nombre=models.CharField(max_length=30, null=False)
    correo=models.CharField(max_length=80, null=False)
    direccion=models.CharField(max_length=30, null=False)
    contraseña=models.CharField(max_length=30, null=False)