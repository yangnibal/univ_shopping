from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Item(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    link = models.TextField()

class Basket(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    item = models.ManyToManyField(Item)

