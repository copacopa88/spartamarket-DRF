from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.EmailField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    birthday=models.DateField(auto_now=False, auto_now_add=False)
    sex=models.CharField(max_length=20, blank=True)
    introduce=models.CharField(max_length=200, blank=True)
    