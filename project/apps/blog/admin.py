from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Comments)
admin.site.register(models.Tag)
admin.site.register(models.PageStatus)


admin.site.site_title = "Pages"
admin.site.site_header = "Cats&Dogs Blog"


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        "status",
        "title",
        "description",
        "image",
        "createdDate",
        "updateDate",
        "get_comments",
        "get_tags",
    )

    list_display_links = ("status",)
    search_fields = ("status.name", "title", "tags.tagName")
    ordering = ("createdDate", "updateDate")
    list_filter = ("status",)
    date_hierarchy = "createdDate"
