from django.urls import re_path,path,include
from .views import index,loginPage,register,logout_user,business,profile



urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('register/', register, name='register'),
    path('profile/',profile, name='profile'),
    path('login/', loginPage, name='login'),
    path('logout/',logout_user,name='logout'),
    path('business/',business, name='business'),
  
]