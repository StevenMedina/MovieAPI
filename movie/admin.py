from django.contrib import admin

from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'created_at',
        'is_recommended',
        'is_active',
    ]

    fieldsets = (
        ('Datos generales', {
            'fields': (
                'name',
                'description',
                'summary',
                'created_at',
                'is_recommended',
                'is_active',
            ),
        }),
    )

    list_filter = ['created_at', 'is_recommended', 'is_active']

    search_fields = ['name']

    readonly_fields = ['created_at']
