from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=122)
    available_quantity = models.CharField(max_length=10)
    price = models.FloatField(max_length=10)
    image = models.ImageField(upload_to='images')
    date = models.DateField()  