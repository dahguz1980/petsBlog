from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from adminblog.models import Page


# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


class BlogList(ListView):
    model = Page
    template_name = "home/pages.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status=True)
        return queryset


class PageDetail(DetailView):
    model = Page
    template_name = "home/detail_page.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status=True)
        return queryset
