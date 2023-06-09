from django import forms

from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control form-control-sm", "style": "width: 50%"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        image = cleaned_data.get("image")

        if not title or not description or not image:
            raise forms.ValidationError("Todos los campos son requeridos.")

        # Realiza otras validaciones personalizadas si es necesario

        return cleaned_data
