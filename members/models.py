from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null = True)
    joined_date = models.DateField(null = True)
    slug = models.SlugField(default="", null=False)

class Product(models.Model):
    productname = models.CharField(max_length=255)
    inventory = models.IntegerField(null = False)
    productpic = models.ImageField(upload_to='statics/')
    price = models.DecimalField(max_digits=8, decimal_places=2)

def __str__(self):
    return f"{self.firstname} {self.lastname}"

def __str__(self):
    return f"{self.productname}"