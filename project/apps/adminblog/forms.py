from django import forms

from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ["user", "title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control form-control-sm", "style": "width: 50%"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")

        if not title or not description:
            raise forms.ValidationError("Todos los campos son requeridos.")

        # Realiza otras validaciones personalizadas si es necesario

        return cleaned_data
