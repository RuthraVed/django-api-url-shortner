from random import choices
from string import ascii_letters

from django.conf import settings
from django.db import models


class Link(models.Model):
    original_link = models.URLField(max_length=1000)
    shortened_link = models.URLField(blank=True, null=True, editable=False)

    def shortlink_generation(self):
        keep_building_url = True
        while keep_building_url:
            random_string = "".join(choices(ascii_letters, k=6))
            new_link = settings.HOST_URL + "/" + random_string

            if Link.objects.filter(shortened_link=new_link).exists():
                continue
            else:
                keep_building_url = False

        return new_link

    def save(self, *args, **kwargs):
        if not self.shortened_link:
            new_link = self.shortlink_generation()
            self.shortened_link = new_link
        return super().save(*args, **kwargs)
