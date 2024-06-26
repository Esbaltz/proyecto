# Generated by Django 5.0.6 on 2024-06-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0015_alter_libro_isbn_alter_libro_tipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='tipo',
            field=models.CharField(choices=[('No_Ficción', 'No_Ficción'), ('Sin tipo', 'Sin tipo'), ('Ficción', 'Ficción')], default='Sin tipo', max_length=30),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado_pedido',
            field=models.CharField(choices=[('Cancelado', 'Cancelado'), ('Entregado', 'Entregado'), ('En proceso', 'En proceso')], default='En proceso', max_length=40),
        ),
    ]
