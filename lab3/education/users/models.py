from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(default=18,
                                      verbose_name='Возраст')
    image = models.ImageField(upload_to='users',
                              default='default.png',
                              max_length=100,
                              verbose_name='Фоточка')
    is_teacher = models.BooleanField(default=False,
                                     verbose_name='Преподаватель')
    # USERNAME_FIELD = 'email'
    # email = models.EmailField(_('email address'),
    #                           unique=True)
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
