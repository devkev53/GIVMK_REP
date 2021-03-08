from django.contrib import admin
from .models import Producto

# Register your models here.

class AdminProduto(admin.ModelAdmin):
    list_display = ['nombre']

admin.site.register(Producto, AdminProduto)