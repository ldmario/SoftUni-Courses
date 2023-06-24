from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from my_exam.myapp.validators import NameOnlyLetters, StartWithLetter


# Create your models here.

class Fruit(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=(
            MinLengthValidator(2),
            NameOnlyLetters(),
        )
    )
    image_url = models.URLField(
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=False,
        null=False,
    )
    nutrition = models.TextField(
        blank=True,
        null=True,
    )


class Profile(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        validators=(
            MinLengthValidator(2),
            StartWithLetter(),
        ),

    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=35,
        validators=(
            MinLengthValidator(1),
            StartWithLetter(),
        ),

    )
    email = models.EmailField(
        blank=False,
        null=False,
        max_length=40,
    )
    password = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=(
            MinLengthValidator(8),
        )
    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )
    age = models.IntegerField(
        blank=False,
        null=False,
        default=18
    )
