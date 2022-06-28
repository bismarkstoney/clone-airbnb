
from django.test import SimpleTestCase
from django.urls import reverse



class BlogPageTest(SimpleTestCase):
    def setUp(self): # new
        url = reverse("blog:home")
        self.response = self.client.get(url)
    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)
