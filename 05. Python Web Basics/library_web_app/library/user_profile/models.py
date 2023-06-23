from django.db import models

# Create your models here.
class Profile(models.Model):
    pass

    first_name = models.CharField(max_length=30)

    last_name = models.CharField(max_length=30)

    image_url = models.URLField()