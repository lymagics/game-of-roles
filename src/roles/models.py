import stripe

from django.conf import settings
from django.db import models

if settings.DEBUG:
    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
else:
    stripe.api_key = settings.STRIPE_LIVE_SECRET_KEY


class IntervalChoices(models.IntegerChoices):
    """
    Choices for subscription interval.
    """
    MONTH = 1, 'Month'
    THREE_MONTHS = 3, 'Three Month'
    YEAR = 12, 'Year'


class Role(models.Model):
    """
    Role entity.
    """
    name = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True)
    price_per_month = models.IntegerField()

    def to_checkout(self, user, interval):
        return stripe.checkout.Session.create(
            mode='subscription',
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
            metadata={
                'user_id': user.pk,
                'role': self.name,
                'interval': interval,
            },
            line_items=[{
                'quantity': 1,
                'price_data': {
                    'currency': settings.CURRENCY,
                    'unit_amount': self.price_per_month,
                    'product_data': {
                        'name': self.name,
                        'description': self.description,
                    },
                    'recurring': {
                        'interval': 'month',
                        'interval_count': interval,
                    },
                },
            }],
        ).url

    def __str__(self) -> str:
        return self.name


class Subscription(models.Model):
    """
    Subscription entity.
    """
    ref = models.CharField(max_length=120)
    interval = models.IntegerField(choices=IntervalChoices.choices,
                                   default=IntervalChoices.MONTH)
    role = models.ForeignKey(Role,
                             on_delete=models.CASCADE,
                             related_name='subscriptions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='subscriptions')

    def __str__(self) -> str:
        return f'Subscription of {self.user} for {self.role}'
