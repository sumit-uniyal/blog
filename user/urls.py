from django.urls import path, include
from .views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('register/', register, name='register'),
    path('login_user/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
]