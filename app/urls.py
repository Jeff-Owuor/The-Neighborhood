from django.urls import re_path,path,include

# from .views import index,RegisterView,LoginView,UserView,LogoutView,RefreshView
from . import views



urlpatterns = [

    re_path(r'^index',views.index,name='index'),
    re_path(r'^$',views.signin,name='signin'),
    re_path(r'^search/',views.search_business,name='search'),
    re_path(r'^signup',views.signup,name='signup'),
    re_path(r'^logout',views.logout,name='logout'),
    re_path(r'^business',views.business,name='business'),
    re_path(r'^profile',views.profile,name='profile'),   
]