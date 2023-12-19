from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CategoryForm, CommentForm
from .models import Category, Item, Comment, Order, OrderItem
import random


def index(request):
    cats = Category.objects.all()
    items = Item.objects.all()
    context = {
        'cats': cats,
        'items': items
    }
    return render(request, 'main/index.html', context=context)


def show_item(request, item_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(name=request.POST["name"], text=request.POST["text"], item_id=item_id)
            comment.save()
        else:
            print("no POST")

    item = Item.objects.get(id=item_id)
    comments = Comment.objects.filter(item=item)

    all_items = Item.objects.filter(category=item.category)
    random_items = random.sample(list(all_items), 3)

    context = {
        "item": item,
        "comments": comments,
        "random_items": random_items,
        "form": CommentForm,
    }
    return render(request, 'main/item.html', context=context)


def item_info(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "main/item.html", context=context)


def show_category(request, category_id):
    category = Category.objects.get(id=category_id)
    items = Item.objects.filter(category=category)
    context = {
        'category': category,
        'items': items
    }
    return render(request, 'main/category.html', context=context)


def category_info(request):
    cats = Category.objects.all()
    context = {
        "cats": cats
    }
    return render(request, "main/category.html", context=context)


def discount_items(request):
    discount = Item.objects.filter(is_sale=True)

    for item in discount:
        item.discounted_price = item.price - (item.price * item.discount / 100)

    context = {
        'discount': discount
    }
    return render(request, 'main/discount.html', context=context)


def order_item(request, item_id):
    try:
        user_order = Order.objects.get(user=request.user)
    except Order.DoesNotExist:
        user_order = Order(user=request.user)
        user_order.save()

    user_item = Item.objects.get(id=item_id)

    new_order_item = OrderItem(order=user_order, item=user_item)
    new_order_item.save()

    return redirect('order')


def order(requests):

    order = Order.objects.get(user__id=requests.user.id)
    items = OrderItem.objects.filter(order=order)
    context = {
        'items': items
    }

    return render(requests, 'main/order.html', context=context)



def new_item(request, item_id):

    new_item = Item.objects.filter().order_by('-item_id')[:5]

    context = {
        "new_item": new_item
    }

    return render(request, 'main/new_item.html', context=context)


def payment(request):
    return render(request, 'main/payment.html')

def delivery(request):
    return render(request, "main/delivery.html")

