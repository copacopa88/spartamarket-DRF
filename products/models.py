from django.conf import settings 
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="image/", null=False)
    price = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return self.title
    