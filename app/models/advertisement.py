from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from app.models.category import Category


class Advertisement(models.Model):
    title = models.TextField()
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='advertisements', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='advertisements', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
