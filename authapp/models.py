from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64)
    username = models.CharField(unique=True, max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.username
