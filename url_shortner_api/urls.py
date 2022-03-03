from django.urls import path

from url_shortner_api.views import ShortenerCreateApiView, ShortenerListAPIView

app_name = "url_shortner_api"

urlpatterns = [
    path("", ShortenerListAPIView.as_view(), name="all_links"),
    path("create/", ShortenerCreateApiView.as_view(), name="create_shortlink"),
]
