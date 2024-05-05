from django.db import models
from users.models import CustomUser
from random import randint

class Category(models.Model):
     image = models.ImageField(upload_to='images/categories/')
     name = models.CharField(max_length=120)

     def __str__(self):
         return self.name

class ItemGender(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/categories/')
    is_sale = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, default=1)
    gender = models.ForeignKey(to=ItemGender, on_delete=models.CASCADE, default=1)
    discount_price = models.FloatField(null=True, blank=True)
    slug = models.CharField(max_length=120, null=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.is_sale:
            self.discount_price = self.price - (self.price * self.discount / 100)
        self.slug = f"{str(randint(1, 999))}-{self.name.replace(' ', '-')}"
        super(Item, self).save(force_insert, force_update, *args, **kwargs)


class ItemImg(models.Model):
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=120)
    imgfield = models.ImageField(upload_to='images/categories/')


class ItemSize(models.Model):
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()

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
    size = models.ForeignKey(to=ItemSize, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"товар: {self.item.name}, размер: {self.size.name}"




class Tag(models.Model):
    name = models.CharField(max_length=120)

class GenderBasicTag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class ItemTag(models.Model):
    item = models.ForeignKey(to='Item', on_delete=models.CASCADE)
    tag = models.ForeignKey(to='Tag', on_delete=models.CASCADE)

class GenderTag(models.Model):
    item = models.ForeignKey(to='Item', on_delete=models.CASCADE)
    tag = models.ForeignKey(to='GenderBasicTag', on_delete=models.CASCADE)

















