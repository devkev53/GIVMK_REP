from django.contrib import admin
from .models import Client, PhoneClient

# Register your models here.
class ModelInlinePhoneClient(admin.TabularInline):
    model = PhoneClient
    fields = ('phone_number', 'is_favorite')
    extra = 0
    min_num = 1

class AdminCLient(admin.ModelAdmin):
    inlines = [ModelInlinePhoneClient,]
    list_display = ['getFullName', 'edad', 'estado', 'toJSON']

admin.site.register(Client, AdminCLient)
admin.site.register(PhoneClient)
