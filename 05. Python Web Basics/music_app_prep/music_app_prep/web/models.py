from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator

from music_app_prep.web.validators import CharAndUnderscoreValidator


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=(MinLengthValidator(2), MaxLengthValidator(15), CharAndUnderscoreValidator()),
        default=None,
    )

    email = models.EmailField(blank=False, null=False, default=None)

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=(MinValueValidator(0),)
    )


class Album(models.Model):
    OPTIONS = [
        ('PopMusic', "PopMusic"),
        ('JazzMusic', "JazzMusic"),
        ('RnBMusic', "R&BMusic"),
        ('RockMusic', "RockMusic"),
        ('Country Music', "Country Music"),
        ('Dance Music', "Dance Music"),
        ('Hip Hop Music', "Hip Hop Music"),
        ('Other', "Other"),
    ]

    album_name = models.CharField(blank=False, null=False, unique=True, max_length=30)

    artist = models.CharField(blank=False, null=False, max_length=30)

    genre = models.CharField(
        choices=OPTIONS,
        blank=False,
        null=False,
        max_length=30,
    )

    description = models.TextField(blank=True, null=True)

    image_url = models.URLField(blank=False, null=False)

    price = models.FloatField(blank=False, null=False, validators=(MinValueValidator(0),))
