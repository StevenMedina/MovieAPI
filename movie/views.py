from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from . import forms, models


class MovieDetailView(LoginRequiredMixin, DetailView):
    template_name = 'movie/movie_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(
            models.Movie,
            pk=self.kwargs['pk'],
            is_active=True,
        )


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = models.Movie
    form_class = forms.MovieForm
    template_name = 'movie/movie_create.html'
    success_url = reverse_lazy('home')


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Movie
    form_class = forms.MovieForm
    template_name = 'movie/movie_update.html'
    success_url = reverse_lazy('home')


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Movie
    success_url = reverse_lazy('home')
