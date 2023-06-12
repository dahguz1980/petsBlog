from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomAuthenticationForm, RegisterForm, UpdateUserForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class LoginRequest(LoginView):
    template_name = "account/login.html"
    form_class = CustomAuthenticationForm
    # success_url = reverse_lazy("home:index")


class RegisterRequest(SuccessMessageMixin, CreateView):
    template_name = "account/register.html"
    form_class = RegisterForm
    model = CustomUser
    success_message = "Registro Exitoso. Por Favor inicie sesión"
    success_url = reverse_lazy("account:login")


class UpdateProfile(LoginRequiredMixin, UpdateView):
    template_name = "account/profile_update.html"
    model = CustomUser
    form_class = UpdateUserForm
    success_url = reverse_lazy("home:index")
