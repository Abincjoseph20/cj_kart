from django.db import models
from mainapp.models import Products
# Create your models here.

class Carts(models.Model):
    cart_id = models.CharField(max_length=100,blank=True)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.cart_id


class Cart_items(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active =models.BooleanField(default=True)


    def __str__(self):
        return self.product