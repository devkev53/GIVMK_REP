# Generated by Django 2.2 on 2021-03-08 01:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreate', models.DateField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('dateUpdate', models.DateField(auto_now=True, null=True, verbose_name='Modification Date')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('precio_consultora', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Precio Consultora')),
                ('precio_catalogo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Precio Catalogo')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Decripción')),
                ('img', models.ImageField(blank=True, null=True, upload_to='Catalogo/', verbose_name='Imagen')),
                ('estado', models.BooleanField(default=False, editable=False, verbose_name='Estado')),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='userCreatecatalogo_producto_related', to=settings.AUTH_USER_MODEL, verbose_name='Creator User')),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='userUpdatecatalogo_producto_related', to=settings.AUTH_USER_MODEL, verbose_name='Modifier User')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]