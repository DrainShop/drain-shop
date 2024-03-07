from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemsAPIView.as_view()),
]