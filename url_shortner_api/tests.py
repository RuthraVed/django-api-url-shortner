from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from url_shortner_api.models import Link

LONG_URL = "https://github.com/RuthraVed/juvoxa"


class Test_Link(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="test_user", password="test@123")
        Link.objects.create(
            original_link=LONG_URL,
        )

    def test_insertion_original_link(self):
        link_obj = Link.objects.get(id=1)
        long_link = f"{link_obj.original_link}"
        self.assertEqual(LONG_URL, long_link)

    def test_shortlink_generation(self):
        link_obj = Link.objects.get(id=1)
        short_link = f"{link_obj.shortened_link}"
        self.assertIn(settings.HOST_URL, short_link)

    def test_check_redirection(self):
        pass


class Test_LinkAPI(APITestCase):
    def test_api_create_short_link(self):
        data = {"original_link": LONG_URL}
        url = reverse("url_shortner_api:create_shortlink")
        response = self.client.post(url, data, format="json")
        self.assertIn(settings.HOST_URL, response.data["shortened_link"])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_non_creation_of_duplicate_original_links(self):
        # Creating 1st short url
        data = {"original_link": LONG_URL}
        url = reverse("url_shortner_api:create_shortlink")
        response_1 = self.client.post(url, data, format="json")

        # Creating 2nd short url, with same long url
        data = {"original_link": LONG_URL}
        url = reverse("url_shortner_api:create_shortlink")
        response_2 = self.client.post(url, data, format="json")

        self.assertEqual(response_1.data["shortened_link"], response_2.data["shortened_link"])
