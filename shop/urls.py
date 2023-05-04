from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index_n")
]

urlpatterns = urlpatterns + [
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/register/", views.register, name='register_n'),
    path("profile/", views.profilis, name='user_profile_n'),

]