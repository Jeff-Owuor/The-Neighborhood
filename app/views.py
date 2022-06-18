from django.shortcuts import render,redirect

from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from .serializers import UserSerializer
from rest_framework.response import Response
from .forms import RegisterForm
from .models import Profile,Business
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .authentication import create_access_token,create_refresh_token,decode_access_token,decode_refresh_token

# Create your views here.


def index(request):
    return render(request,'all_templates/index.html')

def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, 'all_templates/signup.html', {"form":form})


def signin(request):
    context ={}
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            signin(request,user)
            return redirect('index')
    
    return render(request,'all_templates/signin.html',context)

def logout(request):
    logout(request)
    return redirect('login')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, 'registration/register.html', {"form":form})


def loginPage(request):
    context ={}
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
    
    return render(request,'registration/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('login')

def profile(request):
    profile = Profile.objects.get(user=request.user.id)
    form = ProfileEdit(instance=request.user.profile)
    
    if request.method=='POST':
        form = ProfileEdit(request.POST,request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'app/profile.html',{"profile":profile,"form":form})

@login_required(login_url='login')
def business(request):
    user = request.user
    business = Business.objects.filter(neighborhood=user.profile.neighborhood).all()
    form = BusinessForm()
    if request.method=='POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            neighborhood = form.cleaned_data['neighborhood']
            created = Business(image=image, name=name,email=email,neighborhood=neighborhood,user=request.user)
            created.save()
            
    return render(request, 'ip4/business.html',{"title":'Business/Events','form':form,"business":business,'user':user})
