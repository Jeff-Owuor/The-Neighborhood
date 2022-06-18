from django.urls import re_path,path,include
from .views import index,RegisterView,LoginView,UserView,LogoutView,RefreshView
from . import views



urlpatterns = [
    re_path(r'^index',views.index,name='index'),
    path('register/', RegisterView.as_view()),
    re_path(r'^$',views.signin,name='signin'),
    re_path(r'^signup',views.signup,name='signup'),
    re_path(r'^logout',views.logout,name='logout'),
    path('login/',LoginView.as_view()),
    path('user/',UserView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('refresh/',RefreshView.as_view()),    
    
]