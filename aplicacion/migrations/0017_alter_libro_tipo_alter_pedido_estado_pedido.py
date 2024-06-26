# Generated by Django 5.0.6 on 2024-06-27 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0016_alter_libro_tipo_alter_pedido_estado_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='tipo',
            field=models.CharField(choices=[('Ficción', 'Ficción'), ('No_Ficción', 'No_Ficción'), ('Sin tipo', 'Sin tipo')], default='Sin tipo', max_length=30),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado_pedido',
            field=models.CharField(choices=[('En proceso', 'En proceso'), ('Cancelado', 'Cancelado'), ('Entregado', 'Entregado')], default='En proceso', max_length=40),
        ),
    ]
