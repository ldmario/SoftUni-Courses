# Generated by Django 4.2.2 on 2023-06-22 12:36
from django.core.validators import MinValueValidator
from django.db import migrations, models
import music_app_prep.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_profile_age_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='price',
            field=models.FloatField(validators=[MinValueValidator(0)]),
        ),
    ]
