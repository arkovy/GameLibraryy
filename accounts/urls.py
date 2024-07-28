from django.urls import path
from .views import register, user_login

urlpatterns = [
    path('accounts/register/', register, name='signup'),
    path('accounts/login/', user_login, name='login'),
]

