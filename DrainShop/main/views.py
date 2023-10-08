from django.shortcuts import render
from django.http import HttpResponse
from .forms import CategoryForm
from .models import Category


def index(request):
    return render(request, 'main/index.html')


def order(requests):
    return render(requests, 'main/order.html')

def payment(request):
    return render(request, 'main/payment.html')

# def add_category(request):
#     if request.method == "POST":
#         form = CategoryForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     else:
#         form = CategoryForm()
#     return render(request, 'main/add_category.html', {'form': form})
#
# def show_categories(request):
#     cats = Category.objects.all()
#     return render(request, 'main/add_category.html', context={'cats': cats})