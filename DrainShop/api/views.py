from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Item, Comment, Category
from .serializers import ItemSerializer, CommentSerializer, CategorySerializer
from rest_framework import viewsets

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

