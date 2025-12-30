from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Имя')
    email = models.EmailField(unique=True, verbose_name='Email')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
