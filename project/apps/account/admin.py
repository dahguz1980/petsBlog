from django.contrib import admin

# Register your models here.

from . import models

admin.site.site_title = "Accounts"
admin.site.site_header = "Cats&Dogs Blog"


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "description",
        "photo",
        "facebookLink",
        "twitterLink",
        "linkedinLink",
        "createdDate",
        "updateDate",
    )

    list_display_links = ("user",)
    search_fields = ("user.username", "user.first_name", "user.last_name")
    ordering = ("createdDate", "updateDate")
    list_filter = ("user",)
    date_hierarchy = "createdDate"
