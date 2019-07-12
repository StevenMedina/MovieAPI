from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.urls import path

from .forms import UserPasswordResetForm
from .views import UserRegistrationFormView
from .views import CustomLoginView
from .views import RegistrationDoneView


app_name = 'registration'
urlpatterns = [
    path(
        'registro/',
        UserRegistrationFormView.as_view(),
        name='register',
    ),

    path(
        'registro/exitoso/',
        RegistrationDoneView.as_view(),
        name='register_done',
    ),

    path(
        'ingresar/',
        CustomLoginView.as_view(),
        name='login',
    ),

    path(
        'salir/',
        auth_views.LogoutView.as_view(),
        name='logout',
    ),

    path(
        'contraseña/cambiar/',
        auth_views.PasswordChangeView.as_view(),
        name='password_change',
    ),

    path(
        'contraseña/cambiar/hecho/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done',
    ),

    path(
        'contraseña/recuperar/',
        auth_views.PasswordResetView.as_view(
            extra_email_context={'BASE_URL': settings.BASE_URL},
            form_class=UserPasswordResetForm,
            html_email_template_name='registration/password_reset_email.html',
        ),
        name='password_reset',
    ),

    path(
        'contraseña/recuperar/hecho/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),

    path(
        'contraseña/restablecer/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy(settings.LOGIN_REDIRECT_URL),
            post_reset_login=True,
            post_reset_login_backend=settings.AUTHENTICATION_BACKENDS[0],
        ),
        name='password_reset_confirm',
    ),
]
