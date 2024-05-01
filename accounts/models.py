from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    username=models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    birthday=models.DateField(auto_now=False, auto_now_add=False)
    gender=models.CharField(max_length=20, default="", blank=True, null=True)
    introduce=models.CharField(max_length=200, default="", blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile/', default='default.png')
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)