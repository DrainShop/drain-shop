from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from math import floor


def root(request):
    context = {
        'categories': Category.objects.filter(is_active=True),
        'main_banner': MainBanner.objects.first(),
        'secondary_banners': SecondaryBanner.objects.all()[:2],
        'items': Item.objects.all(),

    }
    return render(request, 'home.html', context=context)


def show_items(request):
    model = request.GET.get('model', 'tags')
    value = request.GET.get('value', 'Одеджа')
    if model == "tags":
        tag = Tag.objects.get(name=value)
        item_tags = ItemTag.objects.filter(tag=tag)
        items = Item.objects.filter(id__in=item_tags.values('item_id'))
    if model == "categories":
        category = Category.objects.get(name=value)
        items = Item.objects.filter(category=category)
    if model == "gender":
        items = Item.objects.filter(gender=value)
    context = {
        'value': value,
        'categories': Category.objects.filter(is_active=True),
        'tags': Tag.objects.all(),
        'items': items

    }
    return render(request, 'items.html', context=context)

def show_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        item = None

    cart_items = CartItem.objects.none()
    cart_items_sizes = []

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        cart_items_sizes = cart_items.values_list('item_size_id', flat=True)

    reviews = Review.objects.filter(item=item)

    try:
        total_marks = sum(review.mark for review in reviews)
        review_count = reviews.count()
        average_mark = int(total_marks / review_count)
    except ZeroDivisionError:
        average_mark = 0

    context = {
        'cart_items': cart_items,
        'cart_items_sizes': cart_items_sizes,
        'items': Item.objects.all(),
        'tags': Tag.objects.all(),
        'item': item,
        'reviews': reviews,
        'item_images': ItemImage.objects.filter(item=item),
        'item_sizes': ItemSize.objects.filter(item=item),
        'average_mark': average_mark
    }

    return render(request, 'item.html', context=context)


def show_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)

    total_price = 0
    for cart_item in cart_items:
        total_price += cart_item.item_size.item.default_price * cart_item.amount

    if request.method == "POST":
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            address=request.POST.get('address')
        )

        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                item_size=cart_item.item_size,
                amount=cart_item.amount
            )
            cart_item.delete()

        return redirect(
            f'https://mock-payment.dyussenov.dev/payment?user_id={request.user.id}&order_id={order.id}&price={order.total_price}')

    context = {
        'total_price': total_price,
        'cart_items': cart_items,
        'cart_items_sizes': CartItem.objects.filter(user=request.user).values_list('item_size_id', flat=True),
        'items': Item.objects.all(),
        'tags': Tag.objects.all(),
    }
    return render(request, 'cart.html', context=context)


def show_orders(request):
    context = {
        'tags': Tag.objects.all(),
        'created_orders': Order.objects.filter(user=request.user, status="CREATED_ORDER"),
        'accepted_orders': Order.objects.filter(user=request.user, status="ACCEPTED_ORDER"),
        'delivered_orders': Order.objects.filter(user=request.user, status="DELIVERED_ORDER"),
        'completed_orders': Order.objects.filter(user=request.user, status="COMPLETED_ORDER"),
        'cancelled_orders': Order.objects.filter(user=request.user, status="CANCELLED_ORDER"),
    }
    return render(request, 'orders.html', context=context)


def show_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    context = {
        'tags': Tag.objects.all(),
        'order': order,
        'order_items': order_items
    }
    return render(request, 'order.html', context=context)


def add_to_cart(request, item_id, size_id):
    item = Item.objects.get(id=item_id)
    item_size = ItemSize.objects.get(id=size_id)

    CartItem.objects.create(
        user=request.user,
        item_size=item_size,
        amount=1
    )

    context = {
        'cart_items': CartItem.objects.filter(user=request.user),
        'item_sizes': ItemSize.objects.filter(item=item),
        'cart_items_sizes': CartItem.objects.filter(user=request.user).values_list('item_size_id', flat=True),
    }
    return render(request, 'partials/item-sizes-list.html', context=context)


def delete_from_cart(request, item_id, size_id):
    item = Item.objects.get(id=item_id)
    item_size = ItemSize.objects.get(id=size_id)

    CartItem.objects.get(user=request.user, item_size=item_size).delete()
    context = {
        'cart_items': CartItem.objects.filter(user=request.user),
        'item_sizes': ItemSize.objects.filter(item=item),
        'cart_items_sizes': CartItem.objects.filter(user=request.user).values_list('item_size_id', flat=True),
    }
    return render(request, 'partials/item-sizes-list.html', context=context)


def delete_cart_item(request, item_id, size_id):
    item = Item.objects.get(id=item_id)
    item_size = ItemSize.objects.get(id=size_id)

    CartItem.objects.get(user=request.user, item_size=item_size).delete()
    total_price = 0
    cart_items = CartItem.objects.filter(user=request.user)
    for cart_item in cart_items:
        total_price += cart_item.item_size.item.default_price * cart_item.amount

    context = {
        'total_price': total_price,
        'cart_items': cart_items,
        'item_sizes': ItemSize.objects.filter(item=item),
        'cart_items_sizes': CartItem.objects.filter(user=request.user).values_list('item_size_id', flat=True),
    }
    return render(request, 'partials/cart-items-list.html', context=context)


def change_cart_item_amount(request, item_id, size_id):
    item = Item.objects.get(id=item_id)
    item_size = ItemSize.objects.get(id=size_id)

    cart_item = CartItem.objects.get(user=request.user, item_size=item_size)
    cart_item.amount = request.POST.get('amount')
    cart_item.save()

    total_price = 0
    cart_items = CartItem.objects.filter(user=request.user)
    for cart_item in cart_items:
        total_price += cart_item.item_size.item.default_price * cart_item.amount

    context = {
        'total_price': total_price,
        'cart_items': CartItem.objects.filter(user=request.user),
        'item_sizes': ItemSize.objects.filter(item=item),
        'cart_items_sizes': CartItem.objects.filter(user=request.user).values_list('item_size_id', flat=True),
    }
    return render(request, 'partials/cart-items-list.html', context=context)


def cancel_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.user == order.user and order.status != "COMPLETED_ORDER":
        order.status = "CANCELLED_ORDER"
        order.save()

    return redirect('orders')




def add_review(request, item_id):
    item = Item.objects.get(id=item_id)
    user = request.user

    if OrderItem.objects.filter(order__user=user, item_size__item=item, order__status='COMPLETED_ORDER'):
        mark = request.POST.get("mark")
        text = request.POST.get("text")



        Review.objects.create(
            user=user,
            mark=mark,
            text=text,
            item=item
        )



    reviews = Review.objects.filter(item=item)

    try:
        total_marks = sum(review.mark for review in reviews)
        review_count = reviews.count()
        average_mark = int(total_marks / review_count)
    except ZeroDivisionError:
        average_mark = 0


    context = {
        'cart_items': CartItem.objects.filter(user=request.user),
        'cart_items_sizes': CartItem.objects.filter(user=request.user).values_list('item_size_id', flat=True),
        'items': Item.objects.all(),
        'item': item,
        'reviews': reviews,
        'item_images': ItemImage.objects.filter(item=item),
        'item_sizes': ItemSize.objects.filter(item=item),
        'average_mark': average_mark
    }
    return render(request,'partials/reviews-list.html', context=context)



