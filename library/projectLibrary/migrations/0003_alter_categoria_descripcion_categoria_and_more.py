# Generated by Django 4.1.2 on 2024-07-12 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectLibrary', '0002_delete_alumno_delete_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion_categoria',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='libro',
            name='descripcion_breve',
            field=models.TextField(max_length=500),
        ),
    ]