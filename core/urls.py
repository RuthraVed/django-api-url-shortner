from django.contrib import admin
from django.urls import include, path
from url_shortner_api.views import Redirector

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("url_shortner_api.urls", namespace="url_shortner_api")),
    path("<str:shortener_link>/", Redirector.as_view(), name="redirector"),
]
