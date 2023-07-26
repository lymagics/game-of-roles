from django.conf import settings
from django.db import models


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
