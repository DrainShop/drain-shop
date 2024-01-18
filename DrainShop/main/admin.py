from django.contrib import admin
from .models import Item, Category, Comment, ItemSize, Tag, ItemTag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')

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