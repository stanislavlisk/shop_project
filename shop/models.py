import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from PIL import Image
from .my_utils import generate_thumbnail


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nuotrauka = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    def __str__(self):
        return f" logged as: {self.user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.nuotrauka.path)
        thumb_size = 150
        img_thumb = generate_thumbnail(img, thumb_size, )
        img_thumb.save(self.nuotrauka.path)

    


class ItemCategory(models.Model):
    item_category = models.CharField("Item category", max_length=30, help_text="shop item category name")

class ItemModel(models.Model):
    item_model_name = models.CharField("Item model name", max_length=30, help_text="shop item category name")





