from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='номер телефона')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', null=True, blank=True)
    country = models.CharField(max_length=40, verbose_name='страна')
    generated_key = models.CharField(max_length=30, verbose_name='сгенерированный ключ', null=True, blank=True)
    user_key = models.CharField(max_length=30, verbose_name='ключ верификации', null=True, blank=True)
    is_verified = models.BooleanField(default=False, verbose_name='признак верификации')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
