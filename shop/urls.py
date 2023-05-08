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
    path("view_items_models_list/", views.ItemModelListView.as_view(), name='view_items_models_list_n'),
    path("view_item_model_detail/<int:pk>", views.ItemModelDetailView.as_view(), name='view_item_model_detail_n'),
    ##
    path("administrator/add_item", views.ItemCreateView.as_view(), name='add_item_n'),
    path("administrator/<uuid:pk>/update_item", views.ItemUpdateView.as_view(), name='update_item_n'),
    path("administrator/<uuid:pk>/delete_item", views.ItemDeleteView.as_view(), name='delete_item_n'),
    path("administrator/view_items", views.ItemView.as_view(), name='view_items_list_n'),
    path("administrator/view_orders", views.AdministratorOrderListView.as_view(), name='view_order_list_n'),
    ##
    path("cart/", views.user_cart_view, name='user_cart_n'),
    path("add_to_cart/", views.add_item_to_cart, name='add_item_to_cart_n'),
    path("remove_from_cart/", views.remove_item_from_cart, name='remove_item_from_cart_n'),
    path("cart/increase/", views.increase_item_count, name='increase_quantity_n'),
    path("cart/decrease/", views.decrease_item_count, name='decrease_quantity_n'),
    ##
    path("cart/submit", views.submit_order_by_user, name='submit_order_by_user_n'),
    path("cart/user_orders", views.UserOrderListView.as_view(), name='view_order_by_user_list_n'),


]

urlpatterns = urlpatterns + [
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/register/", views.register, name='register_n'),

]
