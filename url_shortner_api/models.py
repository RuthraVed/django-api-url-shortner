from django.db import models


class Link(models.Model):
    original_link = models.URLField(max_length=1000)
    shortened_link = models.URLField(blank=True, null=True, editable=False)
