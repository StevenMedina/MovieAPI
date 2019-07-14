from django.urls import path

from . import views


app_name = 'movie'
urlpatterns = [
    path(
        '<int:pk>/',
        views.MovieDetailView.as_view(),
        name='detail',
    ),
]