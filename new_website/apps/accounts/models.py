from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    #owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    is_full_name_displayed = models.BooleanField(default=True)

    #details
    bio = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
