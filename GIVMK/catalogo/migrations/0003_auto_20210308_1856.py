# Generated by Django 2.2 on 2021-03-09 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20210308_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Decripción'),
        ),
    ]
