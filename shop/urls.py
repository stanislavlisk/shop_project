from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index_n"),
    path("profile/", views.profilis, name='user_profile_n'),
    path("administrator/", views.administrator_page, name='administrator_n'),
    path("administrator/add_category", views.ItemCategoryCreateView.as_view(), name='add_category_n'),
    path("administrator/<int:pk>/category_update", views.ItemCategoryUpdateView.as_view(), name='update_category_n'),
    path("administrator/add_item", views.ItemModelCreateView.as_view(), name='add_item_model_n'),

]

urlpatterns = urlpatterns + [
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/register/", views.register, name='register_n'),

]
