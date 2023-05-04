from django.contrib import admin

from .models import UserProfile, ItemCategory, ItemModel

admin.site.register(UserProfile)
admin.site.register(ItemCategory)
admin.site.register(ItemModel)
