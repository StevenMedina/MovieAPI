from django.views.generic import TemplateView

from movie.models import Movie


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'object_list': Movie.objects.all(),
        })

        return context