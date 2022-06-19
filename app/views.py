from django.shortcuts import render,redirect

from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from .serializers import UserSerializer
from rest_framework.response import Response
from .forms import RegisterForm, BusinessForm, ProfileEdit
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
            return redirect('signin')
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
    return redirect('signin')

@login_required(login_url = "signin")
def search_business(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        business = Business.objects.filter(name__icontains=searched).all()
        params = {
            'searched':searched,
            'businesses':business
        }
        return render(request, 'all_templates/search.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'all_templates/search.html', {'message': message})

@login_required(login_url='signin')
def profile(request):
    profile = Profile.objects.get(user=request.user.id)
    profile = Profile.objects.all()
    form = ProfileEdit(instance=request.user.profile)
    form = ProfileEdit()
    if request.method=='POST':
        form = ProfileEdit(request.POST,request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'all_templates/profile.html',{"profile":profile,"form":form})

@login_required(login_url='signin')
def business(request):
    user = request.user
    business = Business.objects.filter(neighborhood=user.profile.neighborhood).all()
    business = Business.objects.all()
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
    return render(request, 'all_templates/business.html',{"title":'Business/Events','form':form,"business":business,'user':user})
