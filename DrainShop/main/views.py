from django.shortcuts import render
from django.http import HttpResponse
from .forms import CategoryForm
from .models import Category, Item


def index(request):
    cats = Category.objects.all()
    items = Item.objects.all()
    context = {
        'cats': cats,
        'items': items
    }
    return render(request, 'main/index.html', context=context)





def show_item(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        "item": item
    }
    return render(request, 'main/item.html', context=context)

def item_info(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "main/item.html", context=context)





def show_category(request, category_id):
    cat = Category.objects.get(id=category_id)
    context = {
        "cat": cat
    }
    return render(request, 'main/category.html', context=context)

def category_info(request):
    cats = Category.objects.all()
    context = {
        "cats": cats
    }
    return render(request, "main/category.html", context=context)




def order(requests):
    return render(requests, 'main/order.html')

def payment(request):
    return render(request, 'main/payment.html')

