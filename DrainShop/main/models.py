from django.db import models

class Category(models.Model):
     name = models.CharField(max_length=120)
     image = models.ImageField(upload_to='images/categories/')

class Item(models.Model):
     name = models.CharField(max_length=120)
     price = models.FloatField()
     image = models.ImageField(upload_to='images/categories/')
     is_sale = models.BooleanField(default=False)
     discount = models.IntegerField(default=0)
     category = models.ForeignKey(to=Category, on_delete=models.CASCADE, default=1)


class Comment(models.Model):
     name = models.CharField(max_length=120)
     text = models.TextField()
     item = models.ForeignKey(to=Item, on_delete=models.CASCADE)



