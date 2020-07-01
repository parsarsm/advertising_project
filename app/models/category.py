from django.db import models


class Category(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='subcategories')
    name = models.CharField(max_length=200)
