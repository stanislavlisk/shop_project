from django.contrib import admin
from .models import UserProfile, ItemCategory, ItemModel, Item, Cart, CartItem



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo')

class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('item_category',)

class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('item_model_name', 'price', 'photo')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_model_id', 'status')

class CartAdmin(admin.ModelAdmin):
    list_display = ('id',)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('item_model_id', 'cart_id', 'quantity')





admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(ItemModel, ItemModelAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
