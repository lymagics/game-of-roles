from django.db import models


class Mock(models.Model):
    """
    Mock entity.
    """
    type = models.CharField(max_length=50)
    payload = models.JSONField()

    def __str__(self) -> str:
        return self.type
