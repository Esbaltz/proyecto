# Generated by Django 5.0.6 on 2024-06-21 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0007_alter_libro_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='foto',
            field=models.ImageField(null=True, upload_to='libros', verbose_name='Imagen'),
        ),
    ]
