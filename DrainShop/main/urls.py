from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('order/', order, name="order"),
    path('payment/', payment, name="payment"),
    path('delivery/', delivery, name="delivery"),
    path('items/<int:item_id>/', show_item, name="item"),
    path('category/<int:category_id>/', show_category, name="cat"),
    path('discount/', discount_items, name="discount"),
    path('order_item/<int:item_id>/', order_item, name="order_item"),
    path('new_item', new_item, name="new_item"),
]

