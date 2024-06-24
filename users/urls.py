from django.urls import path, include

from .views import *

urlpatterns = [
    path('signup/', create_user, name='signup'),
    path('', include('django.contrib.auth.urls')),
]
