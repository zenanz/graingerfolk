from django.db import models
from django.contrib.auth.models import User
from website.storage import OverwriteStorage
import os


def image_path(instance, filename):
    return os.path.join('profiles/photo', str(instance.user.id)+'_avatar.ext')

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(storage=OverwriteStorage(),upload_to=image_path,blank=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

