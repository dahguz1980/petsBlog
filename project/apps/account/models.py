from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """User Profle"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, null=False, blank=False)
    photo = models.ImageField(null=True, blank=True)
    facebookLink = models.CharField(max_length=250, null=True, blank=True)
    twitterLink = models.CharField(max_length=250, null=True, blank=True)
    instagramLink = models.CharField(max_length=250, null=True, blank=True)
    linkedinLink = models.CharField(max_length=250, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        """Represent a class instance as a String."""
        return self.user.username
