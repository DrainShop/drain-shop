from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import *
import random
from random import randint
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


@login_required(login_url='login')
def order_item(request, item_id, size_id):
    try:
        user_basket = Basket.objects.get(user=request.user)
    except Basket.DoesNotExist:
        user_basket = Basket.objects.create(user=request.user)

    user_item = Item.objects.get(id=item_id)
    item_size = ItemSize.objects.get(id=size_id)

    # Проверяем, существует ли уже такой товар в корзине
    existing_item = BasketItem.objects.filter(basket=user_basket, item=user_item, size=item_size).first()
    if existing_item:
        existing_item.quantity += 1
        existing_item.total += user_item.price
        existing_item.save()
    else:
        new_basket_item = BasketItem(basket=user_basket, item=user_item, size=item_size, quantity=1,
                                     total=user_item.price)
        new_basket_item.save()

    return redirect('order')


# def delete_order_item(request, order_item_id):
#     try:
#         order_item = OrderItem.objects.get(id=order_item_id)
#     except OrderItem.DoesNotExist:
#         return redirect('order')
#
#     if order_item.order.user != request.user:
#         return redirect('order')
#
#     order_item.delete()
#
#     return redirect('order')



@login_required(login_url='login')
def order(request):
    try:
        basket = Basket.objects.get(user=request.user)
        basket_items = BasketItem.objects.filter(basket=basket)
        items = {}

        total_price_discount = 0
        total_discount = 0

        for basket_item in basket_items:
            key_item = (basket_item.item, basket_item.size)
            if key_item not in items:
                items[key_item] = basket_item.quantity
            else:
                items[key_item] += basket_item.quantity

            if basket_item.item.discount:
                total_price_discount += basket_item.item.price * basket_item.quantity * (1 - basket_item.item.discount / 100)
                total_discount += basket_item.item.discount * basket_item.quantity

        total_price = sum(basket_item.item.price * basket_item.quantity for basket_item in basket_items)

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

        total_item_count = sum(items.values())

        context = {
            "items_list": items_list,
            "tags": tags,  # Если переменная tags используется, она должна быть определена где-то в коде
            "total_price": total_price,
            "total_item_count": total_item_count,
            "total_price_discount": total_price_discount,
            "total_discount": total_discount
        }

    except Basket.DoesNotExist:
        context = {
            "items_list": [],
            "tags": tags,  # Если переменная tags используется, она должна быть определена где-то в коде
            "total_price": 0,
            "total_item_count": 0,
            "total_price_discount": 0,
            "total_discount": 0
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
    tag = get_object_or_404(Tag, id=tag_id)
    items = ItemTag.objects.filter(tag=tag)

    context = {
        "items": items,
        "tag": tag
    }

    return render(request, 'main/tag.html', context=context)

def gender_tag(request, tag_id):
    gender_tags = GenderBasicTag.objects.get(id=tag_id)
    items = GenderTag.objects.filter(tag=tag)

    context = {
        "items": items,
        "gender_tags": gender_tags
    }

    return render(request, 'main/gender_tag.html', context=context)

def payment(request):
    return render(request, 'main/payment.html')


def delivery(request):
    return render(request, "main/delivery.html")


def add_slug(request):
    items = Item.objects.filter(slug=None)
    for item in items:
        item.slug = f"{str(randint(1, 9999))}-{item.name.replace(' ', '-')}"
        item.save()

    return render(request, "main/index.html")
