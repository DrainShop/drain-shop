from django.db import models
from users.models import CustomUser

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


     def __str__(self):
         return self.name

# class ItemSizes(models.Model):
#     item = models.
#     name = models.
#     description =

class Comment(models.Model):
     name = models.CharField(max_length=120)
     text = models.TextField()
     item = models.ForeignKey(to=Item, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ пользователя {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)


















