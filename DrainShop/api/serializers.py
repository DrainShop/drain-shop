from rest_framework import serializers
from main.models import *
from users.models import CustomUser


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class ItemGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGender
        fields = '__all__'

class ItemSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSize
        fields = '__all__'

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'

class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = '__all__'

class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUser
        fields = "__all__"

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class AddToBasketSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    size_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['order', 'delivery_datetime', 'status']



