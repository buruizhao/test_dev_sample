from django.test import TestCase
from project_app.models import Project
from django.contrib.auth.models import User

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('testDev01','testDev01@123.com','test123')

    def test_user(self):
        username = User.objects.get(username='testDev01')
        print(username.email)
        print(username.password)
        self.assertEqual(username.email,'testDev01@123.com')