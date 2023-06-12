from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from . import models, forms

admin.site.site_title = "Accounts"
admin.site.site_header = "Cats&Dogs Blog"


class CustomUserAdmin(UserAdmin):
    add_form = forms.RegisterForm
    form = forms.UpdateUserForm
    model = models.CustomUser
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2", "is_staff", "is_active", "groups", "user_permissions")}),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(models.CustomUser, CustomUserAdmin)
