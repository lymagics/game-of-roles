import factory
from factory.django import DjangoModelFactory

from roles.models import Subscription
from users.tests.factories import UserFactory


class SubscriptionFactory(DjangoModelFactory):
    ref = factory.Faker('isbn13')
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Subscription
