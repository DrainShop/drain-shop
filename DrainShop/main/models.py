from django.db import models

class Category(models.Model):
     name = models.CharField(max_length=120)
     image = models.ImageField(upload_to='images/categories/')




