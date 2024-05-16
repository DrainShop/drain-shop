from .views import *
from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'item-list', ItemsViewSet)
router.register(r'category-list', CategoryViewSet)
router.register(r'item-genders', ItemGenderViewSet)
# router.register(r'item-sizes', ItemSizeViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = [
    # path('items/', ItemsAPIView.as_view()),
    path('check/', CiCheck.as_view()),
    path('ccheck/', CicCheck.as_view()),
    path('', include(router.urls)),
    path('comments/<int:pk>/', AllCommentsAPIView.as_view()),
    path('registration/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
    path('item-sizes/<int:item_id>/', ItemSizeViewSet.as_view({'get': 'list'})),
    path('rand-category/', RandomCategoryAPIView.as_view(), name="rand_item"),
    path('rand-disk/', RandomDiscountAPIView.as_view(), name="rand_disk"),
    path('add-to-basket/', AddToBasketItemAPIView.as_view(), name='add-to-basket'),
    path('create-order/', CreateOrderAPIView.as_view(), name='create-order')
]