from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from website.storage import OverwriteStorage
from django.utils import timezone
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

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=255, default='')
    thumbnail = models.URLField(max_length=255, blank=True, null=True)
    detail = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username + '---' + self.slug
