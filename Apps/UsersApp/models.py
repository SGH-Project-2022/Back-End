from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=255)

    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    phone = models.CharField(max_length=255, unique=True)

    image = models.CharField(max_length=255, null=True)

    country = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    username = None
    first_name = None
    last_name = None
    is_staff = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_user_by_email(email: str):
        return User.objects.filter(email=email).first()
