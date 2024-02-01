from django.contrib import admin
from .models import Item, Category, Comment, ItemSize, Tag, ItemTag, ItemImg
from.forms import ItemForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'category')
    form = ItemForm

@admin.register(ItemImg)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'item', 'imgfield')

@admin.register(Comment)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')

@admin.register(ItemSize)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('description', )

@admin.register(Tag)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ItemTag)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('tag', 'item')