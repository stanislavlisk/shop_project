import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from PIL import Image
from .my_utils import generate_thumbnail

# Item = Product, can't change now! naming mistake

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")
    adress = models.CharField("shipping details", max_length=150, blank=True, null=True)

    def __str__(self):
        return f" logged as: {self.user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        thumb_size = 150
        img_thumb = generate_thumbnail(img, thumb_size, )
        img_thumb.save(self.photo.path)


class ItemCategory(models.Model):
    item_category = models.CharField("Item category", max_length=30, help_text="shop item category name")

    def __str__(self):
        return f"{self.item_category}"

class ItemModel(models.Model):
    item_model_name = models.CharField("Item model name", max_length=30, help_text="shop item category name")
    category_id = models.ManyToManyField("ItemCategory", help_text="Item category")
    price = models.FloatField("Item price", default="0.00")
    photo = models.ImageField(default="item_pics/default.jpg", upload_to="item_pics", null=True)

    def save(self, *args, **kwargs):
        self.price = round(self.price, 2)
        super(ItemModel, self).save(*args, **kwargs)
        img = Image.open(self.photo.path)
        thumb_size = 600
        img_thumb = generate_thumbnail(img, thumb_size)
        img_thumb.save(self.photo.path)

    @property
    def items_left_a(self):
        return len(self.item_set.filter(status='a'))

    @property
    def items_left(self):
        return len(self.item_set.all())



    def __str__(self):
        return f"{self.item_model_name}"


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    item_model_id = models.ForeignKey('ItemModel', on_delete=models.CASCADE, null=True, blank=True)


    ITEM_STATUS = (
        ('u', 'Unavailable'),
        ('a', 'Available'),
        ('r', 'Reserved'),
        ('s', 'Sold'),
    )

    status = models.CharField(
        "Status",
        max_length=1,
        choices=ITEM_STATUS,
        blank=True,
        default='u',
        help_text="Item status"
    )

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


    @property
    def cart_total(self):
        items = [item for item in self.cartitem_set.all()]
        return sum([(i.item_model_id.price * i.calculated_quantity) for i in items])

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    order_comment = models.TextField("Comment", max_length=1000, null=True, blank=True)




class CartItem(models.Model):
    item_model_id = models.ForeignKey('ItemModel', on_delete=models.CASCADE, null=True, blank=True)
    cart_id = models.ForeignKey('Cart', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField("quantity", default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order_id = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, blank=True)


    @property
    def calculated_quantity(self):
        if self.quantity > self.item_model_id.items_left_a:
            return self.item_model_id.items_left_a
        elif self.quantity < 0:
            return 0
        else:
            return self.quantity

    @property
    def calculated_price(self):
        return self.calculated_quantity * self.item_model_id.price

    def save(self, *args, **kwargs):
        if self.quantity > self.item_model_id.items_left_a:
            self.quantity = self.item_model_id.items_left_a
        elif self.quantity < 0:
            self.quantity = 0
        super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return f"item's cart id: {self.cart_id}"



















