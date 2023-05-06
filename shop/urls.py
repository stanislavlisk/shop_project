from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index_n"),
    path("profile/", views.profilis, name='user_profile_n'),
    path("administrator/", views.administrator_page, name='administrator_n'),
    ##
    path("administrator/add_category", views.ItemCategoryCreateView.as_view(), name='add_category_n'),
    path("administrator/<int:pk>/update_category", views.ItemCategoryUpdateView.as_view(), name='update_category_n'),
    path("administrator/<int:pk>/delete_category", views.ItemCategoryDeleteView.as_view(), name='delete_category_n'),
    ##
    path("administrator/add_item_model", views.ItemModelCreateView.as_view(), name='add_item_model_n'),
    path("administrator/<int:pk>/update_item_model", views.ItemModelUpdateView.as_view(), name='update_item_model_n'),
    path("administrator/<int:pk>/delete_item_model", views.ItemModelDeleteView.as_view(), name='delete_item_model_n'),
    path("view_items_list/", views.ItemModelView.as_view(), name='view_items_models_n'),
    ##
    path("administrator/add_item", views.ItemCreateView.as_view(), name='add_item_n'),
    path("view_items/", views.ItemView.as_view(), name='view_items_n'),

]

urlpatterns = urlpatterns + [
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/register/", views.register, name='register_n'),

]
