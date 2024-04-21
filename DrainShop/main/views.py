from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CategoryForm, CommentForm
from .models import Category, Item, Comment, Order, OrderItem, ItemSize, Tag, ItemTag, ItemImg, ItemGender
import random
from random import randint
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

tags = Tag.objects.all()


def index(request):
    all_cat = Category.objects.all()

    all_disks = Item.objects.filter(is_sale=True)

    cats = Category.objects.all()

    items = Item.objects.all()

    for item in items:
        item.calculated_price = item.price - (item.price * item.discount / 100)

    context = {
        'cats': cats,
        'items': items,
        "tags": tags
    }

    if len(all_disks) > 0:
        random_disk = random.sample(list(all_disks), 1)
        context['disk'] = random_disk[0]

    if len(all_cat) > 0:
        random_cats = random.sample(list(all_cat), 1)
        context['rand_item'] = random_cats[0]

    return render(request, 'main/index.html', context=context)


def show_item(request, slug):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(name=request.POST["name"], text=request.POST["text"], slug=slug)
            comment.save()
        else:
            print("no POST")

    item = Item.objects.get(slug=slug)
    comments = Comment.objects.filter(item=item)
    sizes = ItemSize.objects.filter(item=item)
    imgs = ItemImg.objects.filter(item=item)

    all_items = Item.objects.filter(category=item.category)
    num_items_to_sample = max(1, min(3, len(all_items)))
    random_items = random.sample(list(all_items), num_items_to_sample)

    context = {
        "item": item,
        "comments": comments,
        "random_items": random_items,
        "form": CommentForm,
        "sizes": sizes,
        "imgs": imgs,
        "tags": tags,

    }
    print(imgs)
    return render(request, 'main/item.html', context=context)


def item_info(request):
    items = Item.objects.all()
    context = {
        "items": items,
        "tags": tags
    }
    return render(request, "main/item.html", context=context)


def show_category(request, category_id):
    category = Category.objects.get(id=category_id)
    items = Item.objects.filter(category=category)
    context = {
        'category': category,
        'items': items,
        "tags": tags
    }
    return render(request, 'main/category.html', context=context)


def category_info(request):
    cats = Category.objects.all()
    context = {
        "cats": cats,
        "tags": tags
    }
    return render(request, "main/category.html", context=context)


def discount_items(request):
    discount = Item.objects.filter(is_sale=True)

    for item in discount:
        item.discounted_price = item.price - (item.price * item.discount / 100)

    context = {
        'discount': discount,
        "tags": tags
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
    new_order_item = OrderItem(order=user_order, item=user_item, size=item_size)

    new_order_item.save()

    return redirect('order')


@login_required(login_url='login')
def order(request):
    try:
        order = Order.objects.get(user=request.user)
        order_items = OrderItem.objects.filter(order=order)
        items = {}

        for order_item in order_items:
            key_item = (order_item.item, order_item.size)
            if key_item not in items:
                items[key_item] = 1
            else:
                items[key_item] += 1

        total_price = sum(order_item.item.price for order_item in order_items)

        items_list = []
        for key, value in items.items():
            items_list.append(
                {
                    "item": key[0],
                    "size": key[1],
                    "amount": value,
                    "total": value * key[0].price

                }
            )

        context = {
            "items_list": items_list,
            "tags": tags,
            "total_price": total_price
        }

    except Order.DoesNotExist:
        order = None
        context = {
            "items_list": [],
            "tags": tags,
            "total_price": 0
        }

    return render(request, 'main/order.html', context=context)


def new_item(request):
    new_items = Item.objects.all().order_by('-id')[:10]

    context = {
        "new_items": new_items,
        "tags": tags
    }

    return render(request, 'main/new_item.html', context=context)


def tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    items = ItemTag.objects.filter(tag=tag)

    context = {
        "items": items,
        "tags": tags
    }

    return render(request, 'main/tag.html', context=context)


def payment(request):
    return render(request, 'main/payment.html')


def delivery(request):
    return render(request, "main/delivery.html")


def add_slug(request):
    items = Item.objects.filter(slug=None)
    for item in items:
        item.slug = f"{str(randint(1, 999))}-{item.name.replace(' ', '-')}"
        item.save()

    return render(request, "main/delivery.html")
