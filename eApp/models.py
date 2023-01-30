from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ['name']