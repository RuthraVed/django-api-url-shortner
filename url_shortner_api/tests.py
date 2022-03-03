from django.contrib.auth.models import User
from django.test import TestCase

from url_shortner_api.models import Link


class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="test_user", password="test@123")
        Link.objects.create(
            original_link="https://github.com/RuthraVed/juvoxa",
        )

    def test_insertion_original_link(self):
        link_obj = Link.objects.get(id=1)
        long_link = f"{link_obj.original_link}"
        self.assertEqual("https://github.com/RuthraVed/juvoxa", long_link)

    def test_shortlink_generation(self):
        link_obj = Link.objects.get(id=1)
        short_link = f"{link_obj.shortened_link}"
        self.assertIn("http://127.0.0.1:8000/", short_link)

    def test_api_post_original_link(self):
        pass

    def test_api_get_short_link(self):
        pass

    def test_non_creation_of_duplicate_original_links(self):
        pass
