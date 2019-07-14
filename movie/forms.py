from django import forms

from . import models


class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = [
            'name',
            'description',
            'summary',
            'is_recommended',
            'is_active',
        ]