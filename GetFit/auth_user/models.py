from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

class AuthUser(AbstractUser):
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    email = models.EmailField(
        max_length=40,
    )

    username = models.CharField(
        max_length=18,
        unique=True,
    )

    first_name = models.CharField(
        max_length=40,
        validators=(
            MinLengthValidator(2),
        ),
    )

    last_name = models.CharField(
        max_length=40,
        validators=(
            MinLengthValidator(2),
        ),
    )

    age = models.PositiveIntegerField(
        null=True,
    )

    gender = models.CharField(
        choices=GENDERS,
    )

    weight = models.FloatField(
        null=True,
    )

    height = models.PositiveIntegerField(
        null=True,
    )

    profile_picture = models.ImageField(
        null=True,
        blank=True,
    )
