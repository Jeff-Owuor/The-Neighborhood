from django.shortcuts import render,redirect


from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from .serializers import UserSerializer
from django.views.generic.edit import CreateView
from rest_framework.response import Response
from .forms import NeighborhoodForm, RegisterForm,ProfileEdit,BusinessForm,PostForm,CreateProfileForm
from .models import Neighborhood, Profile,Business,Post
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


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


    return render(request, 'all_templates/signup_form.html', {"form":form})


def signin(request):
    context ={}
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
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
    form = ProfileEdit(instance=request.user.profile)
    form = ProfileEdit()
    if request.method=='POST':
        form = ProfileEdit(request.POST,request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'all_templates/profile.html',{"profile":profile,"form":form})



class CreateProfilePage(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'app/create_user_profile.html'
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def business(request):
    user = request.user
    business = Business.objects.filter(neighborhood=user.profile.neighborhood).all()
    return render(request, 'app/business.html',{"title":'Business/Events',"business":business,'user':user})

def businessUpload(request):
    current_user  = request.user
    profile_instance = Profile.objects.get(user=current_user)
    if request.method =='POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = profile_instance
            project.save()
        return redirect('home')
    else:
        form  = BusinessForm()
        context  = {
            "form":form
            }
    return render(request, 'app/post.html', context)


def search_business(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        business = Business.objects.filter(name__icontains=searched).all()
        params = {
            'searched':searched,
            'businesses':business
        }
        return render(request, 'app/search.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'app/search.html', {'message': message})


def postUpload(request):
    current_user  = request.user
    profile_instance = Profile.objects.get(user=current_user)
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = profile_instance
            project.save()
        return redirect('home')
    else:
        form  = PostForm()
        context  = {
            "form":form
            }
    return render(request, 'app/post.html', context)

def create_hood(request):
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighborhoodForm()
    return render(request, 'newhood.html', {'form': form})


def single_hood(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    params = {
        'hood': hood,
        'business': business,
        'posts': posts
    }
    return render(request, 'app/single_hood.html', params)

  
