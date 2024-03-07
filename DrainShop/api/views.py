from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Item
from .serializers import ItemSerializer

class ItemsAPIView(APIView):
    def get(self, request):
        items = Item.objects.all()
        return Response({"items": ItemSerializer(items, many=True).data})