from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("url_shortner_api.urls", namespace="url_shortner_api")),
]
