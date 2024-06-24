from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(ItemSize)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(ItemTag)
admin.site.register(MainBanner)
admin.site.register(SecondaryBanner)

