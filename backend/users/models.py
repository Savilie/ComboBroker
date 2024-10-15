from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .manager import CustomUserManager

# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255, verbose_name='Email адрес')
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    second_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Отчество")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_authenticated = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'second_name', ]

    objects = CustomUserManager()

    def get_full_name(self) -> str:
        """
        Returns the first_name plus the last_name, with a space in between.
        If second_name is provided, it is included in the full name.
        """
        if self.second_name:
            full_name = f'{self.first_name} {self.second_name} {self.last_name}'
        else:
            full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self) -> str:
        """
        Returns the short name for the user.
        """
        return self.first_name
