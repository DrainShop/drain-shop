from django.urls import path
from django.contrib.auth.views import LoginView
from .views import SignUpView
from users.forms import UserLoginForm

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path(
        'login/',views.LoginView.as_view(
            template_name="login.html",
            authentication_form=UserLoginForm
            ),
        name='login'
)
]
