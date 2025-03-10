from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from apps.user.models.managers.objects import UserObjectManager


# Main Section
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserObjectManager()

    class Meta:
        db_table = "user"
        verbose_name = "사용자"
        verbose_name_plural = "사용자 목록"
