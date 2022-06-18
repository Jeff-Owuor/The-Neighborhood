from django.urls import re_path,path,include
from .views import index,loginPage,register,logout_user



urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/',logout_user,name='logout'),
  
]