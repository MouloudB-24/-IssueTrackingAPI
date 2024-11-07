from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinValueValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, age, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")

        if age < 15:
            raise ValueError("Users must be at least 15 years old.")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, age=age, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    age = models.IntegerField(validators=[MinValueValidator(15)])
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["age"]

    def __str__(self):
        return self.username
