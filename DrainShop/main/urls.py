from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('order/', order, name="order"),
    path('payment/', payment, name="payment"),
    path('items/<int:item_id>/', show_item, name="item"),
    path('category/<int:category_id>/', show_category, name="cat")
    # path('add_category/', views.add_category, name="add_category")
]
