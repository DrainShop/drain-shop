from django.db import models

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=128, default='Нет описания')
    image = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Item(models.Model):
    ITEM_GENDER_CHOICES = [
        ("MALE", "мужской"),
        ("FEMALE", "женский"),
        ("UNISEX", "унисекс"),
        ("MALE_CHILD", "детский мужской"),
        ("FEMALE_CHILD", "детский женский"),
    ]

    name = models.CharField(max_length=128)
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)
    preview = models.ImageField(upload_to='images/')
    gender = models.CharField(max_length=128, choices=ITEM_GENDER_CHOICES)
    description = models.TextField(default=None, null=True)
    default_price = models.IntegerField(default=1999)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.gender}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ItemImage(models.Model):
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item.name}"

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"


class ItemSize(models.Model):
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item.name} - {self.name}"

    class Meta:
        verbose_name = "Размер товара"
        verbose_name_plural = "Размеры товаров"


class CartItem(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    item_size = models.ForeignKey(to=ItemSize, on_delete=models.CASCADE, default=1)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_size.item.name}"

    class Meta:
        verbose_name = "Товар корзины"
        verbose_name_plural = "Товары корзин"


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ("CREATED_ORDER", "Заказ создан"),
        ("ACCEPTED_ORDER", "Заказ принят"),
        ("DELIVERED_ORDER", "Заказ доставлен"),
        ("COMPLETED_ORDER", "Заказ завершен"),
        ("CANCELLED_ORDER", "Заказ отменен"),
    ]

    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, default='адрес не указан')
    total_price = models.IntegerField()
    status = models.CharField(max_length=128, choices=ORDER_STATUS_CHOICES, default="CREATED_ORDER")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.created_at}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы пользователя"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    item_size = models.ForeignKey(to=ItemSize, on_delete=models.CASCADE, default=1)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_size.item.name}"

    class Meta:
        verbose_name = "Товар заказа"
        verbose_name_plural = "Товары заказов"

class Review(models.Model):
    mark = models.IntegerField()
    text = models.TextField()
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item.name} - {self.user.username}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class ItemTag(models.Model):
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.name}-{self.item.name}"

    class Meta:
        verbose_name = "Тэг товара"
        verbose_name_plural = "Тэги товаров"


class MainBanner(models.Model):
    preview = models.ImageField(upload_to='images/')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "Главный баннер"
        verbose_name_plural = "Главные баннеры"


class SecondaryBanner(models.Model):
    preview = models.ImageField(upload_to='images/')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "Вторичный баннер"
        verbose_name_plural = "Вторичные баннеры"
