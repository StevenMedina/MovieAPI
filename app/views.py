from django.views.generic import TemplateView

from movie.models import Movie


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_queryset(self):
        queryset = Movie.objects.all()
        if 'is_recommended' in self.request.GET:
            queryset = queryset.filter(is_recommended=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'object_list': self.get_queryset(),
        })

        return context