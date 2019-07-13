from rest_framework import serializers

from . import models


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = [
            'id',
            'name',
            'description',
            'summary',
            'created_at',
            'is_recommended',
            'is_active',
        ]
