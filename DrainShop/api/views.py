from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from users.models import CustomUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import random
from main.models import *
from django_filters.rest_framework import DjangoFilterBackend

"""
class ItemsAPIView(APIView):
    def get(self, request):
        items = Item.objects.all()
        return Response({"items": ItemSerializer(items, many=True).data})
"""


class ItemsViewSet(viewsets.ReadOnlyModelViewSet):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__id']


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentsAPIView(APIView):
    @extend_schema(
        tags=["comments"],
        responses={200: CommentSerializer(many=True)},
        summary="все комменты для айтема",
        description="фысфы"
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
        tags=["rand_category"],
        responses={200: CategorySerializer(many=True)},
        summary="рандомная категория",
        description="http://127.0.0.1:8000/api/v1/rand_disk/"
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
        tags=["rand_discount"],
        responses={200: ItemSerializer(many=True)},
        summary="рандомный айтем, из него достать скидку",
        description="http://127.0.0.1:8000/api/v1/rand-disk/"
    )
    def get(self, request):
        all_disks = Item.objects.all()

        if all_disks.exists():
            random_cats = random.choice(all_disks)
            serializer = ItemSerializer(random_cats)

            return Response(serializer.data)
        else:
            return Response({"message": "Категорий нет"})



class AllCommentsAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        print(request.user)
        item = Item.objects.get(pk=pk)
        all_comments = Comment.objects.filter(item=item)
        return Response({"all_comments": CommentSerializer(all_comments, many=True).data})


class ItemGenderViewSet(viewsets.ModelViewSet):
    queryset = ItemGender.objects.all()
    serializer_class = ItemGenderSerializer


class ItemSizeViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSizeSerializer

    def get_queryset(self):
        return ItemSize.objects.filter(item__id=self.kwargs['item_id'])


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = OrderItemSerializer


"""------------------------------------------------reg---------------------------------------------------------------"""


class UserRegisterAPIView(APIView):
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
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)

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
                    {'error': 'Invalid credentials'},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {'error': 'Username and password are required'},
                status=status.HTTP_400_BAD_REQUEST,
            )


"""------------------------------------------------basket------------------------------------------------------------"""

class AddToBasketItemAPIView(APIView):
    def post(self, request):
        item_id = request.data.get('item_id')
        size_id = request.data.get('size_id')

        try:
            basket = request.user.basket_set.first()
        except Basket.DoesNotExist:
            basket = Basket.objects.create(user=request.user, total=0)


        try:
            item = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            return Response({"error": "Продукт не существует"}, status=status.HTTP_404_NOT_FOUND)

        try:
            basket_item, created = BasketItem.objects.update_or_create(
                basket=basket,
                item=item,
                size_id=size_id,
                defaults={'total': item.price, 'quantity': 1}
            )

        if not created:
            basket_item.quantity += 1
            basket_item.total = basket_item.quantity * item.price
            basket_item.save()

        basket.total =


        return Response({"message": "Товар добавлен"}, status=status.HTTP_201_CREATED)

