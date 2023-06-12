from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("login/", views.LoginRequest.as_view(), name="login"),
    path("newregister/", views.RegisterRequest.as_view(), name="newregister"),
    path("profile/update/<int:pk>", login_required(views.UpdateProfile.as_view()), name="profileupdate"),
    path("logout/", LogoutView.as_view(next_page="home:index"), name="logout"),
]
