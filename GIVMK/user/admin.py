from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            None, {
                'fields': ('img',)
            }
        ),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'userCreate']

admin.site.register(User, CustomUserAdmin)