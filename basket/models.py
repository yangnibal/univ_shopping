from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Item(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    link = models.URLField()
    thumbnail = models.TextField()
    name = models.CharField(max_length=100)
# Create your models here.
