from django.db import models


class Phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    lug = models.SlugField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.ImageField(max_length=100)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
