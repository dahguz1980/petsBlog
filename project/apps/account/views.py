from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomAuthenticationForm

# Create your views here.


class LoginRequest(LoginView):
    template_name = "account/login.html"
    form_class = CustomAuthenticationForm
    # success_url = reverse_lazy("home:index")
