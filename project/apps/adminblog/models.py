# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

from django.conf import settings

class Page(models.Model):
    """Blog Page"""

    page_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name="Titulo Página")
    description = RichTextField(null=False, blank=False, verbose_name="Descripción")
    status = models.BooleanField(default=False, verbose_name="Estado")
    image = models.ImageField(null=True, blank=True, verbose_name="Imagen Principal")
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        """Represent a class instance as a String."""
        return self.title
