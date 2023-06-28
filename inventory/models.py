from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100)
    identifier = models.CharField(max_length=10, null=True)

class Address(models.Model):
    mainStreet= models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=10)
    zipCode=models.FloatField()

