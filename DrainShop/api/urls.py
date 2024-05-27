from .views import *
from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('comments/<int:pk>/', AllCommentsAPIView.as_view()),
    path('registration/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
    path('item-sizes/<int:item_id>/', ItemSizeViewSet.as_view({'get': 'list'})),
    path('rand-category/', RandomCategoryAPIView.as_view(), name="rand_item"),
    path('rand-disk/', RandomDiscountAPIView.as_view(), name="rand_disk"),
    path('add-to-basket/', AddToBasketItemAPIView.as_view(), name='add-to-basket'),
    path('create-order/', CreateOrderAPIView.as_view(), name='create-order'),
    path('item-genders/', ItemGenderAPIView.as_view(), name='item-gender-list'),
    path('item-sizes/<int:item_id>/', ItemSizeAPIView.as_view(), name='item-size-list'),
    path('items/', ItemsAPIView.as_view(), name='item-list'),
    path('categories/', CategoryAPIView.as_view(), name='category-list'),
    path('basket-item/', ViewBasketItemAPIView.as_view(), name='list-basket-item'),
    path('basket/', ViewBasketAPIView.as_view(), name='basket/'),
    path('list-order/', ListOrderAPIView.as_view(), name="list-order"),

    # path('orders/', OrderAPIView.as_view(), name='order-list'),
    # path('orders/<int:pk>/', OrderAPIView.as_view(), name='order-detail'),
    # path('order-items/', OrderItemAPIView.as_view(), name='order-item-list'),
]

