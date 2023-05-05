from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index_n"),
    path("profile/", views.profilis, name='user_profile_n'),
    path("administrator/", views.administrator_page, name='administrator_n'),
    path("administrator/add_category", views.ItemCategoryCreateView.as_view(), name='add_category_n'),
]

urlpatterns = urlpatterns + [
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/register/", views.register, name='register_n'),

]
