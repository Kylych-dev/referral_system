from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager

class CustomUser(AbstractBaseUser):
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30)
    last_name = models.CharField(('last name'), max_length=30)


    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = ("user")
        verbose_name_plural = ("users")


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"