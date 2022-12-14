from django.db import models
from autoslug import AutoSlugField


class Phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    slug = AutoSlugField(populate_from='name')
    price = models.PositiveIntegerField()
    image = models.ImageField(max_length=100)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField(default=False)

