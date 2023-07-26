from django.urls import reverse

from faker import Faker
from rest_framework.test import APITestCase

from users.tests.factories import UserFactory


class TestUserAPI(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.url_me = reverse('api:auth:rest_user_details')
        cls.faker = Faker()

    def test_retrieving_authenticated_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_me)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['username'], self.user.username)
        self.assertEqual(data['email'], self.user.email)

    def test_not_retrieving_authenticated_user(self):
        response = self.client.get(self.url_me)
        self.assertEqual(response.status_code, 401)

    def test_updating_authenticated_user(self):
        new_data = {
            'username': self.faker.user_name(),
            'email': self.faker.email(),
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.put(self.url_me, new_data)
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, new_data['username'])
        self.assertEqual(self.user.email, new_data['email'])

    def test_not_updating_authenticated_user(self):
        new_data = {
            'username': self.faker.user_name(),
            'email': self.faker.email(),
        }
        response = self.client.put(self.url_me, new_data)
        self.assertEqual(response.status_code, 401)
