from django.urls import path
from .views import *

urlpatterns = [
    path('', views.index, name="home"),
    path('order/', views.order, name="order"),
    path('payment/', views.payment, name="payment"),
    path('items/<int:item_id>/', show_item, name="item")
    # path('add_category/', views.add_category, name="add_category")
]
