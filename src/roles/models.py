from django.db import models


class Role(models.Model):
    """
    Role entity.
    """
    name = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True)
    price_per_month = models.IntegerField()

    def __str__(self) -> str:
        return self.name
