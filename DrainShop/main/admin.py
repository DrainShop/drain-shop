from django.contrib import admin
from .models import Item, Category, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')

@admin.register(Comment)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')