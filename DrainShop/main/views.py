from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CategoryForm, CommentForm
from .models import Category, Item, Comment, Order, OrderItem, ItemSize
import random


def index(request):

    all_cat = Category.objects.all()
    random_cats = random.sample(list(all_cat), 1)

    all_disks = Item.objects.filter(is_sale=True)
    random_disk = random.sample(list(all_disks), 1)

    cats = Category.objects.all()
    items = Item.objects.all()

    context = {
        'cats': cats,
        'items': items,
        "disk": random_disk[0],
        "rand_item": random_cats[0],
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
    sizes = ItemSize.objects.filter(item=item)

    all_items = Item.objects.filter(category=item.category)
    num_items_to_sample = max(1, min(3, len(all_items)))
    random_items = random.sample(list(all_items), num_items_to_sample)

    context = {
        "item": item,
        "comments": comments,
        "random_items": random_items,
        "form": CommentForm,
        "sizes": sizes
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


def order_item(request, item_id, size_id):
    try:
        user_order = Order.objects.get(user=request.user)
    except Order.DoesNotExist:
        user_order = Order(user=request.user)
        user_order.save()

    user_item = Item.objects.get(id=item_id)
    item_size = ItemSize.objects.get(id=size_id)
    new_order_item = OrderItem(order=user_order, item=user_item,size=item_size)

    new_order_item.save()

    return redirect('order')


def order(requests):

    order = Order.objects.get(user__id=requests.user.id)
    order_items = OrderItem.objects.filter(order=order)
    items = {}

    for order_item in order_items:
        key_item = (order_item.item, order_item.size)
        if key_item not in items:
            items[key_item] = 1
        else:
            items[key_item] += 1

    items_list = []
    for key, value in items.items():
        items_list.append(
            {
                "item": key[0],
                "size": key[1],
                "amount": value
            }
        )


    context = {
        "itens_llist": items_list
    }

    return render(requests, 'main/order.html', context=context)



def new_item(request):

    new_items = Item.objects.all().order_by('-id')[:10]

    context = {
        "new_items": new_items
    }

    return render(request, 'main/new_item.html', context=context)

def accessories(request):

    all_accessories = Category.objects.get(id=7)

    context = {
        "all_accessories": all_accessories
    }

    return render(request, 'main/accessories.html', context=context)

def clothes(request):

    all_clothes = Item.objects.filter(category__id__in=[6, 5, 2, 1])

    context = {
        "all_clothes": all_clothes
    }

    return render(request, 'main/clothes.html', context=context)

def shoes(request):

    all_shoes = Item.objects.filter(category__id__in=[3, 4])

    context = {
        "all_shoes": all_shoes
    }

    return render(request, 'main/shoes.html', context=context)

def payment(request):
    return render(request, 'main/payment.html')

def delivery(request):
    return render(request, "main/delivery.html")
