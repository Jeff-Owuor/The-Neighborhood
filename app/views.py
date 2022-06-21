from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from .serializers import UserSerializer
from django.views.generic.edit import CreateView,UpdateView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from .forms import NeighborhoodForm, RegisterForm,ProfileEdit,BusinessForm,PostForm,CreateProfileForm
from .models import Neighborhood, Profile,Business,Post
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


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
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')
    return render(request,'all_templates/signin.html')

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
    return render(request, 'all_templates/profile.html',{"profile":profile})

def business(request):
    user = request.user
    business = Business.objects.filter(neighborhood=user.profile.neighborhood).all()
    return render(request, 'all_templates/business.html',{"title":'Business/Events',"business":business,'user':user})

def businessUpload(request):
    current_user  = request.user
    hood = Neighborhood.objects.get(id=current_user.profile.neighborhood.id)
    profile_instance = Profile.objects.get(user=current_user)
    if request.method =='POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.neighborhood = hood
            project.user = profile_instance
            project.save()
        return redirect('business')
    else:
        form  = BusinessForm()
        context  = {
            "form":form
            }
    return render(request, 'all_templates/upload_business.html', context)

def post(request):
    user = request.user
    post = Post.objects.filter(hood=user.profile.neighborhood).all()
    return render(request, 'all_templates/post.html',{"posts":post})

def postUpload(request):
    current_user  = request.user
    hood = Neighborhood.objects.get(id=current_user.profile.neighborhood.id)
    profile_instance = Profile.objects.get(user=current_user)
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.neighborhood = hood
            project.user = profile_instance
            project.save()
        return redirect('post')
    else:
        form  = PostForm()
        context  = {
            "form":form
            }
    return render(request, 'all_templates/post_form.html', context)

def neighborhood_occupants(request, neighborhood_id):
    hood = Neighborhood.objects.get(id=neighborhood_id)
    members = Profile.objects.filter(neighbourhood=hood)
    return render(request, 'all_templates/members.html', {'members': members})

def create_hood(request):
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('create_hood')
    else:
        form = NeighborhoodForm()
    return render(request, 'all_templates/newhood_form.html', {'form': form})

def neigborhoods(request):
    hoods = Neighborhood.objects.all()
    hoods = hoods[::-1]
    context = {
        'hoods': hoods,
    }
    return render(request, 'all_templates/all_neighborhoods.html', context)

def join_neighborhood(request, id):
    neighbourhood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = neighbourhood
    request.user.profile.save()
    return redirect('index')

def leave_neighborhood(request, id):
    hood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('neigborhoods')



class CreateProfilePage(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'all_templates/create_user_profile.html'
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class EditProfileView(UpdateView):
    model = Profile
    template_name = 'all_templates/edit_profile.html'
    fields = ['bio','username','email','image']
    success_url = reverse_lazy('profile')