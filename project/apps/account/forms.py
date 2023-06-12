from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "Credenciales inválidas. Por favor, verifica tus datos.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["password"].widget.attrs.update({"class": "form-control"})


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "password1", "password2"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control form-control-sm"}),
            "first_name": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            "last_name": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control form-control-sm"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control form-control-sm"}),
        }


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "avatar", "password")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            "last_name": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("password")
