from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Board(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
