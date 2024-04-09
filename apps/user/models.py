from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.user.managers import CustomUserManager


class UserModel(AbstractUser):
    """Модель пользователя."""

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'user_user'

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    login = models.CharField(max_length=20, unique=True, null=False, blank=False)
    first_name = None
    last_name = None
    email = None

    objects = CustomUserManager()
