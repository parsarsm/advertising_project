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


class Advertisement(models.Model):
    # Fields
    title = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='advertisements', on_delete=models.CASCADE)
    date1 = models.DateTimeField(null=True, blank=True)
    date2 = models.DateTimeField(null=True, blank=True)


class Category(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL,blank=True, null=True, related_name='subcategories')
    name = models.CharField(max_length=200)
    # description = models.CharField(max_length=500, null=True,default='')


# class Location():
#     pass

# class Category(models.Model):
#     # Fields
#     name = models.CharField(max_length=30)
#     parent_category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
#
#     def display_parent_category(self):
#         if self.parent_category is None:
#             return 'root'
#
#         now = self.parent_category
#         temp = f'{now.name}'
#         while True:
#             p = now.parent_category
#             if p is None:
#                 temp += f' <- root'
#                 break
#             else:
#                 temp += f' <- {p.name}'
#                 now = now.parent_category
#
#         a = temp.split(' <- ')
#         a.reverse()
#         return '  >  '.join(a)
#
#     display_parent_category.short_description = 'parent_category'
