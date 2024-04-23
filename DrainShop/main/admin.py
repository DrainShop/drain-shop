from django.contrib import admin
from .models import Item, Category, Comment, ItemSize, Tag, ItemTag, ItemImg, ItemGender, Order, OrderItem
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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item', 'size')
