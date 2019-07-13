from django.db import models


class Movie(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='nombre',
        unique=True,
    )

    description = models.TextField(
        max_length=300,
        verbose_name='descripción',
    )

    summary = models.TextField(
        max_length=500,
        verbose_name='resumen',
    )

    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='fecha de creación',
    )

    is_recommended = models.BooleanField(
        default=False,
        verbose_name='es recomendada',
    )

    is_active = models.BooleanField(
        default=False,
        verbose_name='activa',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'película'
        verbose_name_plural = 'películas'
