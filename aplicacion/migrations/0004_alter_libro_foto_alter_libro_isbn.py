# Generated by Django 5.0.6 on 2024-06-14 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_alter_libro_foto_alter_libro_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='foto',
            field=models.ImageField(null=True, upload_to='personas', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='isbn',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
