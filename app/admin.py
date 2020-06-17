from django.contrib import admin

from app.models import Category, Advertisement


admin.site.register(Category)
# admin.site.register(Advertisement)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'display_parent_category')
#     list_filter = ('id', 'name')
#
#
@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'owner', 'image', 'category', 'active')
    list_filter = ('id', 'title', 'description', 'owner', 'image', 'category', 'active')
    # fields = ['title', ('date1', 'date2')]
