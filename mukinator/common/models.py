from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    region = models.CharField(max_length=20)
    email = models.EmailField(max_length=45, unique=True)