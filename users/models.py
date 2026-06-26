from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email address')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='phone number')
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True,
                               verbose_name='Фото/Аватар пользователя')
    country = models.CharField(max_length=100, blank=True, null=True,
                               verbose_name='Страна проживания',
                               help_text='Имя страны проживания пользователя')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

