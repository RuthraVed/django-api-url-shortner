from random import choices
from string import ascii_letters, digits

from django.conf import settings
from django.db import models

AVAILABLE_CHARS = ascii_letters + digits
STR_LENGTH = 7

class Link(models.Model):
    original_link = models.URLField(max_length=1000)
    shortened_link = models.URLField(blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.shortened_link:
            self.shortened_link = shortlink_generation(self)
        return super().save(*args, **kwargs)


def generate_random_string(chars, desired_length):
    return "".join(choices(chars, k=desired_length))


def shortlink_generation(model_instance):
    model = model_instance.__class__
    keep_building_url = True

    while keep_building_url:
        random_string = generate_random_string(chars=AVAILABLE_CHARS, desired_length=STR_LENGTH)
        new_link = settings.HOST_URL + "/" + random_string

        if model.objects.filter(shortened_link=new_link).exists():
            continue
        else:
            keep_building_url = False

    return new_link
