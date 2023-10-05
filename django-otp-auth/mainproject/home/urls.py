from django.urls import path
from home.views import *
urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('otp/', otp, name='otp'),
]