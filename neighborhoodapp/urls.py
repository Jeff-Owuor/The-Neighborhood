from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^index',views.index,name='index'),
    re_path(r'^signup',views.signup,name='signup'),
    re_path(r'^$',views.signin,name='signin'),
    re_path(r'^logout',views.logout,name='logout'),
    re_path(r'^search/',views.search,name='search'),
    re_path(r'^profile',views.profile,name = "profile"),
]