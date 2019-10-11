from django.db import models
from jsonfield import JSONField

# Create your models here.


class Orders(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.IntegerField()
    Add= models.CharField(max_length=100)
    Order=JSONField()
    Price=models.IntegerField()
    Status=models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)

class Locations(models.Model):
    Name=models.CharField(max_length=50)
    ImageUri=models.TextField()
    About=models.CharField(max_length=20)

class Restaurant(models.Model):
    Name=models.CharField(max_length=50)
    ImageUri=models.TextField()
    About=models.CharField(max_length=50)


class FoodList(models.Model):
    Name=models.CharField(max_length=50)
    Price=models.IntegerField()
    Type=models.CharField(max_length=50, null=True)


