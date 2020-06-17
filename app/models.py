from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile data
    phone_number = models.CharField(max_length=15)


class Category(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='subcategories')
    name = models.CharField(max_length=200)


class Advertisement(models.Model):
    title = models.TextField()
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='advertisements', on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True)
    category = models.ForeignKey(Category, related_name='advertisements', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
