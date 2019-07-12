from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserAuthenticationForm(AuthenticationForm):
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={'type': 'email', 'autofocus': True}
        )


class UserPasswordResetForm(PasswordResetForm):
    required_css_class = 'required'

    def get_users(self, email):
        active_users = User.objects.filter(
            email__iexact=email,
            is_active=True,
        )
        return (u for u in active_users)


class UserRegistrationFormMixin(forms.Form):
    required_css_class = 'required'
    required_fields = [
        'email',
        'first_name',
        'last_name',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.required_fields:
            self.fields[field].required = True

    def clean_email(self):
        return self.cleaned_data['email'].strip().lower()

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip().title()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip().title()


class UserRegistrationForm(UserRegistrationFormMixin, UserCreationForm):
    next = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
