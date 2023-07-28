from django.urls import reverse

from rest_framework.test import APITestCase

from mocks.tests.factories import SubscriptionFactory
from roles.models import Role
from users.tests.factories import UserFactory


class TestMockAPI(APITestCase):
    fixtures = ('roles.yaml',)

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.url_premium = reverse('api:mocks:mocks-phone')
        cls.url_extra = reverse('api:mocks:mocks-color')
        cls.url_luxe = reverse('api:mocks:mocks-passport')

    def test_phone_data_can_be_accessed_only_by_premium(self):
        role = Role.objects.get(name='Premium')
        SubscriptionFactory(user=self.user, role=role)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_premium)
        self.assertEqual(response.status_code, 200)

    def test_color_data_can_be_accessed_only_by_extra(self):
        role = Role.objects.get(name='Extra')
        SubscriptionFactory(user=self.user, role=role)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_extra)
        self.assertEqual(response.status_code, 200)

    def test_passport_data_can_be_accessed_only_by_luxe(self):
        role = Role.objects.get(name='Luxe')
        SubscriptionFactory(user=self.user, role=role)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_luxe)
        self.assertEqual(response.status_code, 200)

    def test_can_not_access_data_with_no_subscription(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_premium)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_extra)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_luxe)
        self.assertEqual(response.status_code, 403)
