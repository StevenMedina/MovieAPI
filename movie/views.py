from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from . import models


class MovieDetailView(LoginRequiredMixin, DetailView):
    template_name = 'movie/movie_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(
            models.Movie,
            pk=self.kwargs['pk'],
            is_active=True,
        )
