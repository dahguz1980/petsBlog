from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


from . import models, forms

# Create your views here.


class PagesList(ListView):
    model = models.Page
    template_name = "adminblog/pages.html"

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Page.objects.filter(user=self.request.user, title__icontains=query)
        else:
            query = super().get_queryset()
            object_list = query.filter(user=self.request.user)
        return object_list


class PageCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = models.Page
    template_name = "adminblog/page_create.html"
    form_class = forms.PageForm
    success_url = reverse_lazy("adminblog:pages")
    success_message = "Página Creada Correctamente"

    def form_valid(self, form: forms.PageForm):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PageDetail(DetailView):
    model = models.Page
    template_name = "adminblog/preview.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class PageUpdate(SuccessMessageMixin, UpdateView):
    model = models.Page
    success_url = reverse_lazy("adminblog:pages")
    form_class = forms.PageForm
    template_name = "adminblog/page_create.html"
    success_message = "Página Actualizada Correctamente"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def form_valid(self, form: forms.PageForm):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PageDelete(SuccessMessageMixin, DeleteView):
    model = models.Page
    success_url = reverse_lazy("adminblog:pages")
    success_message = "Página Eliminada Correctamente"
    template_name = "adminblog/page_confirm_delete.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class PagePublish(View):
    def get(self, request, page_id, new_status):
        # Obtener la instancia de la página de blog
        blog_page = get_object_or_404(models.Page, page_id=page_id)

        # Cambiar el estado de publicación
        blog_page.status = new_status
        blog_page.save()

        if new_status == "True":
            messages.success(request, "La página fue publicada")
        else:
            messages.success(request, "La página fue despublicada")

        # Redirigir a la lista de blogs después de la publicación
        return redirect("adminblog:pages")
