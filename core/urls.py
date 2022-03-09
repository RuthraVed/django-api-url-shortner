from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from url_shortner_api.views import Redirector

schema_view = get_schema_view(
    openapi.Info(
        title="URL Shortner using Django DRF",
        default_version="v1",
        description="A url shortner web API.",
        terms_of_service="https://opensource.org/licenses/gpl-license",
        contact=openapi.Contact(email="abhishek44dev@gmail.com"),
        license=openapi.License(name="GPL License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("api/", include("url_shortner_api.urls", namespace="url_shortner_api")),
    path("<str:shortener_link>/", Redirector.as_view(), name="redirector"),
]
