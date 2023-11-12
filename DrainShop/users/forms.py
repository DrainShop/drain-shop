from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

        widgest = {
            'username': forms.TextInput(attrs={
                'class': 'register',
                'placeholder': 'Введите login'
            }
            ),
            'email': forms.TextInput(attrs={
                'class': 'email',
                'placeholder': 'Введите email'
            }
            )
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

