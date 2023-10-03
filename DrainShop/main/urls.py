from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('order/', views.order, name="order"),
    path('payment/', views.payment, name="payment")
]
