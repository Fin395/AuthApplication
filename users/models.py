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
        permissions = [
            ('can_add_homework', 'Может создавать домашку'),
            ('can_update_homework', 'Может редактировать домашку'),
            ('can_view_homework', 'Может просматривать домашку'),
            ('can_delete_homework', 'Может удалять домашку'),
        ]

    def __str__(self):
        return self.email
