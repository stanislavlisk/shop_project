from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, ItemCategory, ItemModel, Item, CartItem, Cart




class ItemCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ItemCategory
        fields = ['item_category']
        widgets = {'form_user': forms.HiddenInput(),}



class ItemModelCreateForm(forms.ModelForm):
    category_id = forms.ModelMultipleChoiceField(
        queryset=ItemCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = ItemModel
        fields = ['item_model_name', 'category_id', 'price', 'photo']
        widgets = {'form_user': forms.HiddenInput(),}

####
class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_model_id', 'status']
        widgets = {'form_user': forms.HiddenInput(),}


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']




