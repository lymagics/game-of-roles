from django.urls import reverse

from rest_framework.test import APITestCase

from roles.models import Role
from users.tests.factories import UserFactory


class TestRoleAPI(APITestCase):
    fixtures = ('roles.yaml',)

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.url = reverse('api:roles:roles-list')

    def test_retrieving_list_of_roles(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        for role in Role.objects.all():
            self.assertContains(response, role)
