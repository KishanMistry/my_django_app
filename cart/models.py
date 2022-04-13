from django.db import models

from home.models import Product

# Create your models here.
class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    quantity = models.IntegerField(default=1)
    price = models.FloatField(max_length=10)
    date = models.DateField()  

def __str__(self):
    return self.id