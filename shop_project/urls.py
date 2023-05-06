
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("app/", include("shop.urls")),
    path("", RedirectView.as_view(url="app/", permanent=True)),
] + static (settings.STATIC_URL, document_root = settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

