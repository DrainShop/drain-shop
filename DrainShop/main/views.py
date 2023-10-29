from django.shortcuts import render
from django.http import HttpResponse
from .forms import CategoryForm, CommentForm
from .models import Category, Item, Comment


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
            comment = Comment(name="qqq", text="bbb", item_id=item_id)
            comment.save()


    item = Item.objects.get(id=item_id)
    comments = Comment.objects.filter(item_id=item_id)
    context = {
        "item": item,
        "comments": comments,
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

