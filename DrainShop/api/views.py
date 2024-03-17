from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Item, Comment
from .serializers import ItemSerializer, CommentSerializer

class ItemsAPIView(APIView):
    def get(self, request):
        items = Item.objects.all()
        return Response({"items": ItemSerializer(items, many=True).data})

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

