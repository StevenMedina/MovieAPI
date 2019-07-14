from django.urls import path

from . import views


app_name = 'movie'
urlpatterns = [
    path(
        'crear/',
        views.MovieCreateView.as_view(),
        name='create',
    ),

    path(
        'detalle/<int:pk>/',
        views.MovieDetailView.as_view(),
        name='detail',
    ),

    path(
        'actualizar/<int:pk>/',
        views.MovieUpdateView.as_view(),
        name='update',
    ),

    path(
        'eliminar/<int:pk>/',
        views.MovieDeleteView.as_view(),
        name='delete',
    ),
]