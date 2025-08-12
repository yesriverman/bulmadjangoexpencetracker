from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'profession', 'kids', 'wife', 'city']

class CustomAuthenticationForm(AuthenticationForm):
    pass  # Uses default username/password fields
