from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    
    def __str__(self):
        return self.category_name

class Item(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_link = models.TextField()
    item_thumbnail = models.ImageField()

    def __str__(self):
        return self.item_thumbnail

class Basket(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    basket_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)

# Create your models here.
