from .views import *
from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'itemlist', ItemsViewSet)
router.register(r'categorylist', CategoryViewSet)
router.register(r'item-genders', ItemGenderViewSet)
router.register(r'item-sizes', ItemSizeViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = [
    # path('items/', ItemsAPIView.as_view()),
    path('', include(router.urls)),
    path('comments/<int:pk>/', AllCommentsAPIView.as_view()),
    path('registration/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='user_login')
]