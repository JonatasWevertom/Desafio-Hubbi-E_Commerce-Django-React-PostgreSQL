from django.db import models
from datetime import datetime

# User
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

# Store
class Store(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

# Product
class Product(models.Model):
    title = models.CharField(max_length=500)
    storeId = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    
class ProductImg(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)

class Cart(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class CartItem(models.Model):
    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    
def upload_location(instace, filename):
    ext = filename.split(".")[-1]
    return "%s/%s.%s" % ("img", datetime.now, ext)

class FileUpload(models.Model):
    imgFile = models.ImageField(upload_to = upload_location)
        