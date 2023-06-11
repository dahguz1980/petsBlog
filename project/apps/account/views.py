from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomAuthenticationForm, RegisterForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.


class LoginRequest(LoginView):
    template_name = "account/login.html"
    form_class = CustomAuthenticationForm
    # success_url = reverse_lazy("home:index")


class RegisterRequest(SuccessMessageMixin, CreateView):
    template_name = "account/register.html"
    form_class = RegisterForm
    success_message = "Registro Exitoso. Por Favor inicie sesión"
    success_url = reverse_lazy("account:login")
