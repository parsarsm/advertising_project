from django.contrib import admin

from app.models import Category, Advertisement


admin.site.register(Category)
admin.site.register(Advertisement)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'display_parent_category')
#     list_filter = ('id', 'name')
#
#
# @admin.register(Advertisement)
# class AdvertisementAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'date1', 'date2')
#     list_filter = ('id', 'title', 'date1', 'date2')
#     fields = ['title', ('date1', 'date2')]
