from django.contrib import admin

from .models import UserProfile, ItemCategory, ItemModel, Item, Cart

admin.site.register(UserProfile)
admin.site.register(ItemCategory)
admin.site.register(ItemModel)
admin.site.register(Item)
admin.site.register(Cart)
