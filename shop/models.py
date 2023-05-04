from django.db import models
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.username}"

    


class ItemCategory(models.Model):
    item_category = models.CharField("Item category", max_length=30, help_text="shop item category name")

class ItemModel(models.Model):
    item_model_name = models.CharField("Item model name", max_length=30, help_text="shop item category name")





