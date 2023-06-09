from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("login/", views.LoginRequest.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="home:index"), name="logout"),
]
