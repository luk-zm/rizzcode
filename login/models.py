from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    xp = models.IntegerField(default=0)
    lvl = models.IntegerField(default=1)
