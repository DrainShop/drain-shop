from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

"""
class ItemsAPIView(APIView):
    def get(self, request):
        items = Item.objects.all()
        return Response({"items": ItemSerializer(items, many=True).data})
"""

class ItemsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CommentsAPIView(APIView):
    @extend_schema(
        tags =  ["comments"],
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

class AllCommentsAPIView(APIView):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        all_comments = Comment.objects.filter(item=item)
        return Response({"all_comments": CommentSerializer(all_comments, many=True).data})

class ItemGenderViewSet(viewsets.ModelViewSet):
    queryset = ItemGender.objects.all()
    serializer_class = ItemGenderSerializer

class ItemSizeViewSet(viewsets.ModelViewSet):
    queryset = ItemSize.objects.all()
    serializer_class = ItemSizeSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer













"""------------------------------------------------reg---------------------------------------------------------------"""


