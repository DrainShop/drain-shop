from django.urls import path
from .views import *


urlpatterns = [
    path('', root, name='home'),
    path('items/<int:item_id>/', show_item, name='item'),
    path('cart/', show_cart, name='cart'),
    path('orders/', show_orders, name='orders'),
    path('orders/<int:order_id>/', show_order, name='order'),
    path('items/', show_items, name='items'),
    path('orders/<int:order_id>/cancel/', cancel_order, name='cancel-order'),
    path('review/<int:item_id>/', add_review, name='add-review')
]
htmx_patterns = [
    path('cart/<int:item_id>/<int:size_id>/', add_to_cart, name='add-to-cart'),
    path('cart/<int:item_id>/<int:size_id>/delete/', delete_from_cart, name='delete-from-cart'),
    path('cart-items/<int:item_id>/<int:size_id>/delete/', delete_cart_item, name='delete-cart-item'),
    path('cart-items/<int:item_id>/<int:size_id>/update/', change_cart_item_amount,
         name='change-cart-item-amount'),
]

urlpatterns += htmx_patterns
