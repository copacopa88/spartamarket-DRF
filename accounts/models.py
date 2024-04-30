from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username=models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    birthday=models.DateField(auto_now=False, auto_now_add=False)
    gender=models.CharField(max_length=20, default="", blank=True, null=True)
    introduce=models.CharField(max_length=200, default="", blank=True, null=True)
    