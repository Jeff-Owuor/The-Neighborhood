from django.urls import re_path,path,include
from .views import register,index,RegisterView



urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('register/', RegisterView.as_view()),
    
]