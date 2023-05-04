from django import forms
from django.contrib.auth.models import User

from .models import UserProfile, ItemCategory


class ItemCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ItemCategory
        fields = ['item_category']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']