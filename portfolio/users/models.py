from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    second_name = models.CharField(max_length=128, default="None")
    website = models.CharField(max_length=128, default='')
    telegram = models.CharField(max_length=64, default='')
    github = models.CharField(max_length=256, default='')
    city = models.CharField(max_length=128, default='')
    phone = models.CharField(max_length=20, default='')