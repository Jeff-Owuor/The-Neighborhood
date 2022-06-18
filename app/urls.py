from django.urls import re_path,path,include
from .views import index,RegisterView,LoginView,UserView,LogoutView,RefreshView



urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('register/', RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('user/',UserView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('refresh/',RefreshView.as_view()),    
    
]