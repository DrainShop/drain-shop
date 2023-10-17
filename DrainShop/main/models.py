from django.db import models

class Category(models.Model):
     name = models.CharField(max_length=120)
     image = models.ImageField(upload_to='images/categories/')

class Item(models.Model):
     name = models.CharField(max_length=120)
     price = models.FloatField()
     image = models.ImageField(upload_to='images/categories/')





