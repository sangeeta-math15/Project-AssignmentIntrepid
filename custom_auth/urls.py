from django.urls import path
from .views import register_user, user_login, user_logout

urlpatterns = [
    path('auth/register/', register_user, name='register'),
    path('auth/login/', user_login, name='login'),
    path('auth/logout/', user_logout, name='logout'),
]

