from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.BlogList.as_view(), name="index"),
    path("detail/<int:pk>", views.PageDetail.as_view(), name="detail_page"),
]
