from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def order(requests):
    return render(requests, 'main/order.html')

# Create your views here.
