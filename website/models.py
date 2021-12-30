from django.db import models
from django.contrib.auth.models import User
from django.db.models import AutoField
from dal import autocomplete

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    achat = models.IntegerField(default=0)
    e_mail= models.EmailField(max_length=254,default='')
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=400, null=True)


    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='PENDING')

    def __str__(self):
        return self.customer.name + " , " + self.product.name




