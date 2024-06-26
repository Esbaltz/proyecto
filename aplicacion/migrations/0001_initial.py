# Generated by Django 5.0.6 on 2024-06-14 03:47

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('isbn', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('foto', models.ImageField(null=True, upload_to='personas', verbose_name='Imagen')),
                ('precio', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('numero_pedido', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad_un_producto', models.PositiveIntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion.libro')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion.pedido')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='comprador_carrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion.usuario'),
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion.libro')),
                ('comprador_carrito', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion.usuario')),
            ],
        ),
    ]
