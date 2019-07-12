from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'is_active',
    )

    list_filter = (
        'is_staff',
        'is_active',
    )

    search_fields = (
        'first_name',
        'last_name',
        'email',
    )

    add_fieldsets = (
        ('Información de acceso', {
            'fields': (
                'email',
                'password1',
                'password2',
            ),
        }),
        ('Información personal', {
            'fields': (
                'first_name',
                'last_name',
            ),
        }),
        ('Permisos', {
            'fields': (
                'is_active',
            ),
        }),
    )

    fieldsets = (
        ('Información de acceso', {
            'fields': (
                'email',
                'password',
            ),
        }),
        ('Información personal', {
            'fields': (
                'first_name',
                'last_name',
            ),
        }),
        ('Permisos', {
            'fields': (
                'is_active',
                'is_staff',
                'groups',
            ),
        }),
        ('Fechas importantes', {
            'fields': (
                'last_login',
                'created_at',
            ),
        }),
    )

    readonly_fields = [
        'last_login',
        'created_at',
    ]

    ordering = ('-id',)
