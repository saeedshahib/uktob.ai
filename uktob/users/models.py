from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(AbstractUser):
    cell_phone = models.CharField(max_length=20)
