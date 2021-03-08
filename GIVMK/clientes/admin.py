from django.contrib import admin
from .models import Client


class AdminCLient(admin.ModelAdmin):
    list_display = ['getFullName', 'edad', 'estado', 'toJSON']

admin.site.register(Client, AdminCLient)
