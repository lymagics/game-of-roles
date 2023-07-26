from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    User entity.
    """
    about_me = models.TextField(default='', blank=True)

    def __str__(self) -> str:
        return self.username
