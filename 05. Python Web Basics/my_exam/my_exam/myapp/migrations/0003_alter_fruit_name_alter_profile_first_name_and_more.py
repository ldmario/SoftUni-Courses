# Generated by Django 4.2.2 on 2023-06-24 09:48

import django.core.validators
from django.db import migrations, models
import my_exam.myapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_nutrition_fruit_nutrition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), my_exam.myapp.validators.NameOnlyLetters()]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), my_exam.myapp.validators.StartWithLetter()]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1), my_exam.myapp.validators.StartWithLetter()]),
        ),
    ]
