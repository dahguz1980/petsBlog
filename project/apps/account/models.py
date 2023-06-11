from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """User Profle"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    photo = models.ImageField(upload_to="avatars", null=True, blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        """Represent a class instance as a String."""
        return self.user.username
