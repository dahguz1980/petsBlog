from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView


from . import models, forms

# Create your views here.


class PagesList(ListView):
    model = models.Page
    template_name = "blog/pages.html"

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Page.objects.filter(title__icontains=query)
        else:
            object_list = models.Page.objects.all()
        return object_list


class PageCreate(CreateView):
    model = models.Page
    template_name = "blog/page_create.html"
    form_class = forms.PageForm
    success_url = reverse_lazy("blog:pages")
