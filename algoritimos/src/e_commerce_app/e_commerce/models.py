from django.db import models

# Create your models here.


class User(models.Model):
    name = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    key = models.TextField(max_length=100)

class Product(models.Model):
    name = models.TextField(max_length=100)
    value = models.TextField(max_length=100)
    amount = models.IntegerField(max_length=100)
