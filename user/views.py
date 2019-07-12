from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic import TemplateView

from .forms import UserAuthenticationForm
from .forms import UserRegistrationForm


class CustomLoginView(LoginView):
    form_class = UserAuthenticationForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'next': self.request.GET.get('next'),
        })

        return context


class UserRegistrationFormView(FormView):
    form_class = UserRegistrationForm
    template_name = 'registration/registration_form.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial.update(self.request.GET.dict())
        return initial

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()

        user = authenticate(
            username=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password1'),
        )
        login(self.request, user)

        self.request.session['register_done'] = True

        if 'next' in form.cleaned_data and form.cleaned_data['next']:
            return redirect('{}?next={}'.format(
                reverse('registration:register_done'),
                form.cleaned_data['next'],
            ))

        return redirect('registration:register_done')


class RegistrationDoneView(TemplateView):
    template_name = 'registration/registration_form_done.html'

    def get(self, request, *args, **kwargs):
        if 'register_done' not in self.request.session:
            return redirect('home')

        del self.request.session['register_done']

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'next': self.request.GET.get('next'),
        })

        return context
