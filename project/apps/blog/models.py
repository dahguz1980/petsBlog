# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField


class Comments(models.Model):
    """Page Comments"""

    comment_id = models.AutoField(primary_key=True)
    comment = models.TextField(null=False, blank=False)
    commentDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        """Represent a class instance as a String."""
        return self.comment_id


class Page(models.Model):
    """Blog Page"""

    page_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name="Titulo Página")
    description = RichTextField(null=False, blank=False, verbose_name="Descripción")
    status = models.BooleanField(default=False, verbose_name="Estado")
    image = models.ImageField(null=False, blank=False, verbose_name="Imagen Principal")
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField(Comments, blank=True)

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        """Represent a class instance as a String."""
        return self.title

    def get_comments(self):
        return "\n".join([c.comments for c in self.comments.all()])
