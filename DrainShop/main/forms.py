from django import forms
from .models import Item, Category, Comment
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'image', 'is_sale', 'discount', "category", "gender", 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
    
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-item',
                'placeholder': 'Ваше имя'
            }
            ),
            'text': forms.TextInput(attrs={
                'class': 'form-item',
                'placeholder': 'Ваш комментарий'
            }
            )
        }