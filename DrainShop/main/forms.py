from django import forms
from .models import Item, Category, Comment
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'image', 'is_sale', 'discount']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']