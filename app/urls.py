from django.urls import re_path,path,include
from django.contrib import admin
from . import views

urlpatterns = [

    re_path(r'^index',views.index,name='index'),
    re_path(r'^$',views.signin,name='signin'),
    re_path(r'^search/',views.search_business,name='search'),
    re_path(r'^signup',views.signup,name='signup'),
    re_path(r'^logout',views.logout,name='logout'),
    re_path(r'^postUpload$',views.postUpload,name='postUpload'),
    re_path(r'^businessUpload',views.businessUpload,name='businessUpload'),
    re_path(r'create_hood', views.create_hood,name='create_hood'),
    path('join_hood/<id>', views.join_neighborhood, name='join-hood'),
    path('leave_hood/<id>', views.leave_neighborhood, name='leave-hood'),   
    re_path(r'^business/',views.business,name='business'),
    re_path(r'^profile',views.profile,name='profile'),  
    re_path(r'^post',views.post,name='post'),  
    re_path(r'^edit_profile',views.edit_profile,name='edit_profile'),
    path('neigborhoods/', views.neigborhoods, name='neigborhoods'), 
    path('<hood_id>/neighborhood_occupants', views.neighborhood_occupants, name='members'), 

]