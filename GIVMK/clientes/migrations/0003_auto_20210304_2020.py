# Generated by Django 2.2 on 2021-03-05 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20210304_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='nacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='client',
            name='NIT',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='NIT'),
        ),
    ]
