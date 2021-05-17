from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(default=18)
    image = models.ImageField(upload_to='users', default='default.png', max_length=100)

    def __str__(self):
        return self.username
