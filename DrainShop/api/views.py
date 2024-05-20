from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from users.models import CustomUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import random
from django.db import transaction
from main.models import *
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend


class OrderAPIView(APIView):
    @extend_schema(
        tags=["orders"],
        responses={200: OrderUserSerializer(many=True)},
        summary="Получение списка всех заказов",
        description="http://127.0.0.1:8000/api/v1/orders/"
    )
    def get(self, request):
        orders = Basket.objects.all()
        serializer = OrderUserSerializer(orders, many=True)
        return Response(serializer.data)

    @extend_schema(
        tags=["orders"],
        request=OrderUserSerializer,
        responses={201: OrderUserSerializer},
        summary="Создание нового заказа",
        description="http://127.0.0.1:8000/api/v1/orders/"
    )
    def post(self, request):
        serializer = OrderUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderItemAPIView(APIView):
    @extend_schema(
        tags=["order-items"],
        responses={200: BasketItemSerializer(many=True)},
        summary="Получение списка всех элементов заказа",
        description="http://127.0.0.1:8000/api/v1/order-items/"
    )
    def get(self, request):
        order_items = BasketItem.objects.all()
        serializer = BasketItemSerializer(order_items, many=True)
        return Response(serializer.data)

    @extend_schema(
        tags=["order-items"],
        request=BasketItemSerializer,
        responses={201: BasketItemSerializer},
        summary="Создание нового элемента заказа",
        description="http://127.0.0.1:8000/api/v1/order-items/"
    )
    def post(self, request):
        serializer = BasketItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemGenderAPIView(APIView):

    @extend_schema(
        tags=["item-genders"],
        responses={200: ItemGenderSerializer(many=True)},
        summary="Получение списка всех категорий по гендерному признаку",
        description="http://127.0.0.1:8000/api/v1/item-genders/"
    )
    def get(self, request):
        item_genders = ItemGender.objects.all()
        serializer = ItemGenderSerializer(item_genders, many=True)
        return Response(serializer.data)

    @extend_schema(
        tags=["item-genders"],
        request=ItemGenderSerializer,
        responses={201: ItemGenderSerializer},
        summary="Создание новой категории по гендерному признаку",
        description="http://127.0.0.1:8000/api/v1/item-genders/"
    )
    def post(self, request):
        serializer = ItemGenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemSizeAPIView(APIView):

    @extend_schema(
        tags=["item-sizes"],
        parameters=[
            OpenApiParameter('item_id', OpenApiTypes.INT, OpenApiParameter.PATH, description='ID товара')
        ],
        responses={200: ItemSizeSerializer(many=True)},
        summary="Получение списка размеров для конкретного товара",
        description="http://127.0.0.1:8000/api/v1/item-sizes/<int:item_id>/"
    )
    def get(self, request, item_id):
        item_sizes = ItemSize.objects.filter(item__id=item_id)
        serializer = ItemSizeSerializer(item_sizes, many=True)
        return Response(serializer.data)

    @extend_schema(
        tags=["item-sizes"],
        parameters=[
            OpenApiParameter('item_id', OpenApiTypes.INT, OpenApiParameter.PATH, description='ID товара')
        ],
        request=ItemSizeSerializer,
        responses={201: ItemSizeSerializer},
        summary="Создание нового размера для конкретного товара",
        description="http://127.0.0.1:8000/api/v1/item-sizes/<int:item_id>/"
    )
    def post(self, request, item_id):
        data = request.data.copy()
        data['item'] = item_id
        serializer = ItemSizeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemSizeViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSizeSerializer
    def get_queryset(self):
        return ItemSize.objects.filter(item__id=self.kwargs['item_id'])

class ItemsAPIView(APIView):
    @extend_schema(
        tags=["items"],
        parameters=[
            OpenApiParameter('category__id', OpenApiTypes.INT, OpenApiParameter.QUERY, description='ID категории')
        ],
        responses={200: ItemSerializer(many=True)},
        summary="Получение списка всех товаров, с возможностью фильтрации по категории",
        description="http://127.0.0.1:8000/api/v1/items/"
    )
    def get(self, request):
        items = Item.objects.all()
        filter_backends = [DjangoFilterBackend]

        for backend in list(filter_backends):
            items = backend().filter_queryset(request, items, view=self)

        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


class CategoryAPIView(APIView):
    @extend_schema(
        tags=["categories"],
        responses={200: CategorySerializer(many=True)},
        summary="Получение списка всех категорий",
        description="http://127.0.0.1:8000/api/v1/categories/"
    )
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CommentsAPIView(APIView):
    @extend_schema(
        tags=["comments"],
        request=CommentSerializer,
        responses={200: CommentSerializer},
        summary="Создание нового комментария",
        description="http://127.0.0.1:8000/api/v1/comments/"
    )
    def post(self, request):
        item = Item.objects.get(pk=request.data["item"])
        new_comment = Comment.objects.create(
            name=request.data["name"],
            text=request.data["text"],
            item=item
        )
        return Response({"new_comment": CommentSerializer(new_comment).data})

class RandomCategoryAPIView(APIView):
    @extend_schema(
        tags=["categories"],
        responses={200: CategorySerializer},
        summary="Получение случайной категории",
        description="http://127.0.0.1:8000/api/v1/random-category/"
    )
    def get(self, request):
        all_cats = Category.objects.all()

        if all_cats.exists():
            random_cats = random.choice(all_cats)
            serializer = CategorySerializer(random_cats)

            return Response(serializer.data)
        else:
            return Response({"message": "Категорий нет"})

class RandomDiscountAPIView(APIView):
    @extend_schema(
        tags=["items"],
        responses={200: ItemSerializer},
        summary="Получение случайной скидки",
        description="http://127.0.0.1:8000/api/v1/random-discount/"
    )
    def get(self, request):
        all_disks = Item.objects.all()

        if all_disks.exists():
            random_cats = random.choice(all_disks)
            serializer = ItemSerializer(random_cats)

            return Response(serializer.data)
        else:
            return Response({"message": "Товаров нет"})

class AllCommentsAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["comments"],
        responses={200: CommentSerializer(many=True)},
        summary="Получение всех комментариев по ID товара",
        description="http://127.0.0.1:8000/api/v1/all-comments/<int:pk>/"
    )
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        all_comments = Comment.objects.filter(item=item)
        return Response({"all_comments": CommentSerializer(all_comments, many=True).data})




"""------------------------------------------------reg---------------------------------------------------------------"""


class UserRegisterAPIView(APIView):
    @extend_schema(
        tags=["users"],
        responses={201: "Токен создан"},
        summary="Регистрация нового пользователя",
        description="http://127.0.0.1:8000/api/v1/register/"
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        new_user = CustomUser.objects.create_user(username=username, password=password)

        basket = Basket.objects.create(user=new_user, total=0)

        return Response(
            {
                'token': 'token created',
            },
            status=status.HTTP_201_CREATED,
        )

class UserLoginAPIView(APIView):
    @extend_schema(
        tags=["users"],
        responses={200: "Токен"},
        summary="Авторизация пользователя",
        description="http://127.0.0.1:8000/api/v1/login/"
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                token = Token.objects.create(user=user)
                return Response(
                    {
                        'token': token.key,
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {'error': 'Неверные учетные данные'},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {'error': 'Имя пользователя и пароль обязательны'},
                status=status.HTTP_400_BAD_REQUEST,
            )


"""------------------------------------------------basket------------------------------------------------------------"""

class AddToBasketItemAPIView(APIView):
    @extend_schema(
        tags=["basket"],
        request={"item_id": "integer", "size_id": "integer"},
        responses={201: BasketSerializer},
        summary="Добавление товара в корзину",
        description="http://127.0.0.1:8000/api/v1/add-to-basket/"
    )
    def post(self, request):
        item_id = request.data.get('item_id')
        size_id = request.data.get('size_id')

        try:
            basket = Basket.objects.get(user=request.user)
        except Basket.DoesNotExist:
            basket = Basket.objects.create(user=request.user, total=0)

        try:
            item = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            return Response({"error": "Продукт не существует"}, status=status.HTTP_404_NOT_FOUND)

        basket_item, created = BasketItem.objects.get_or_create(
            basket=basket,
            item=item,
            size_id=size_id,
            defaults={'total': item.price, 'quantity': 1}
        )

        if not created:
            basket_item.quantity += 1
            basket_item.total = basket_item.quantity * item.price
            basket_item.save()

        basket.total = sum(item.total for item in basket.basketitem_set.all())
        basket.save()

        serializer = BasketSerializer(basket)
        basket_item_serializer = BasketItemSerializer(basket.basketitem_set.all(), many=True)

        return Response({"message": "Товар добавлен",
                         'basket': serializer.data,
                         'basket_items': basket_item_serializer.data
                         }, status=status.HTTP_201_CREATED)

class CreateOrderAPIView(APIView):
    @extend_schema(
        tags=["orders"],
        responses={201: OrderUserSerializer},
        summary="Создание заказа",
        description="http://127.0.0.1:8000/api/v1/create-order/"
    )
    def post(self, request):
        user = request.user

        basket = Basket.objects.filter(user=user).first()
        if not basket:
            return Response({'error': 'Корзина пользователя не найдена'}, status=status.HTTP_400_BAD_REQUEST)

        basket_items = BasketItem.objects.filter(basket=basket)
        if not basket_items:
            return Response({'error': 'Элементы корзины не найдены'}, status=status.HTTP_400_BAD_REQUEST)

        total_amount = basket.total

        order_datetime = timezone.now()

        order = OrderUser.objects.create(
            basket=basket,
            total_amount=total_amount,
            order_datetime=order_datetime
        )

        with transaction.atomic():
            basket.total = 0
            basket.save()

            basket_items.delete()

        serializer = OrderUserSerializer(order)

        return Response({"message": "Заказ создан", "data": serializer.data}, status=status.HTTP_201_CREATED)




