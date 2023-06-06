from django.db import models


# Create your models here.
class PageStatus(models.Model):
    """Page Status"""

    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = "Page Status"
        verbose_name_plural = "Page Statuses"

    def __str__(self):
        """Represent a class instance as a String."""
        return self.name


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


class Tag(models.Model):
    """Tag"""

    tag_id = models.AutoField(primary_key=True)
    tagName = models.CharField(max_length=10, null=False, blank=False)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        """Represent a class instance as a String."""
        return self.tagName


class Page(models.Model):
    """Blog Page"""

    page_id = models.AutoField(primary_key=True)
    status = models.ForeignKey(PageStatus, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="categoría")
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField(Comments, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        """Represent a class instance as a String."""
        return self.title

    def get_comments(self):
        return "\n".join([c.comments for c in self.comments.all()])
    
    def get_tags(self):
        return "\n".join([t.tag for t in self.tags.all()])
