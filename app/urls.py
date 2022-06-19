from django.urls import re_path,path,include
from . import views



urlpatterns = [

    re_path(r'^index',views.index,name='index'),
    re_path(r'^$',views.signin,name='signin'),
    re_path(r'^signup',views.signup,name='signup'),
    re_path(r'^logout',views.logout,name='logout'),
    path('search_business/', views.search_business , name='search_business'),
    path('welfarepost/', views.postUpload ,  name='postUpload'),
    path('businesspost/', views.businessUpload ,  name='businessUpload'),     
    
]