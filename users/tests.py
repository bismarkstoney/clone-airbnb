from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class CustomUserTest(TestCase):
    def test_create_user(self):
        Users=get_user_model()
        user = Users.objects.create_user(username='kkk', email="bk@gmail.com", password='1234')
        self.assertEqual(user.username, 'kkk')
        self.assertEqual(user.email, 'bk@gmail.com')
        self.assertTrue(user.is_active)
    