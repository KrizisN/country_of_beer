from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AuthUserForm, CreateUserForm


class LoginUserView(LoginView):
    """View for authentication users"""

    template_name = 'account/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('#')


class RegisterUserView(CreateView):
    """View for register users"""

    model = User
    template_name = 'account/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('#')



