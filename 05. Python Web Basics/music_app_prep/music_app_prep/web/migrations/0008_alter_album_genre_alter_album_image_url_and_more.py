# Generated by Django 4.2.2 on 2023-06-23 00:09

import django.core.validators
from django.db import migrations, models
import music_app_prep.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_remove_album_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('PopMusic', 'PopMusic'), ('JazzMusic', 'JazzMusic'), ('RnBMusic', 'R&BMusic'), ('RockMusic', 'RockMusic'), ('Country Music', 'Country Music'), ('Dance Music', 'Dance Music'), ('Hip Hop Music', 'Hip Hop Music'), ('Other', 'Other')], max_length=30),
        ),
        migrations.AlterField(
            model_name='album',
            name='image_url',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default=None, max_length=15, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(15), music_app_prep.web.validators.CharAndUnderscoreValidator()]),
        ),
    ]
