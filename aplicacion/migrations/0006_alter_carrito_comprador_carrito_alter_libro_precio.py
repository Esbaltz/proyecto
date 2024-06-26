# Generated by Django 5.0.6 on 2024-06-21 01:56

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_alter_libro_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='comprador_carrito',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='aplicacion.usuario'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='precio',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
