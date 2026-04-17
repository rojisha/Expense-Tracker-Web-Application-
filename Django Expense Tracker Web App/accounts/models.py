from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model (preferred by task).
    Currently identical to AbstractUser, but keeps the project extensible.
    """

    pass
