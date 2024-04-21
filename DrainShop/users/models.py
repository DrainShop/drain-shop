from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
