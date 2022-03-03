from django.contrib import admin

from url_shortner_api.models import Link


@admin.register(Link)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "shortened_link", "original_link")
