from django.db import models
from django.contrib.auth.models import User

# Create your models here
TYPES = (
    ("shoes", "shoes"),
    ("shirt", "shirt"),
    ("skirt", "skirt"),
    ("trouser", "trouser"),
    ("jacket", "jacket"),
    ("other", "other"),
    )
class Item(models.Model):
    image = models.ImageField()
    caption = models.TextField()
    price = models.CharField(max_length=20)
    trending = models.BooleanField(default=False)
    brand = models.CharField(max_length=50)
    formen = models.BooleanField(default=True)
    what = models.CharField(max_length=20, choices=TYPES, default="other")

class MyCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    pending = models.BooleanField(default=True)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)