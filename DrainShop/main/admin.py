from django.contrib import admin
from .models import *
from.forms import ItemForm



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(ItemGender)
class ItemGenderAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'category', 'gender', 'description', )
    form = ItemForm

@admin.register(ItemImg)
class ItemImgAdmin(admin.ModelAdmin):
    list_display = ('name', 'item', 'imgfield')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')

@admin.register(ItemSize)
class ItemSizeAdmin(admin.ModelAdmin):
    list_display = ('description', )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ItemTag)
class ItemTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'item')

@admin.register(GenderBasicTag)
class GenderTagAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(GenderTag)
class GenderTagAdmin(admin.ModelAdmin):
    list_display = ('item', 'tag')

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total')
    search_fields = ('user__username',)
    list_filter = ('created_at',)

@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'basket', 'item', 'size', 'quantity', 'total')
    list_filter = ('basket', 'item', 'size')

@admin.register(OrderUser)
class OrderUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'basket', 'order_datetime', 'total_amount')
    list_filter = ('order_datetime',)
    search_fields = ('basket__user__username',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item', 'size')
    list_filter = ('user', 'item', 'size')
    search_fields = ('user__username',)