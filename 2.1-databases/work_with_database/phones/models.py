from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=30, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.URLField(unique=True)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200, unique=True)
