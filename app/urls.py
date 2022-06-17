from django.urls import re_path,path,include
from .views import register,index



urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('register/', register, name='register'),
    
]