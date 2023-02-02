from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField()

    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ['name']

class Order(models.Model):
    items = models.JSONField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phoneNumber = models.IntegerField()
    totalPrice = models.IntegerField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.items

    
    class Meta:
        ordering = ['items']


