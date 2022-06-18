from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from .forms import RegisterForm,BusinessForm,ProfileEdit
from .models import Profile,Business
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request,'app/index.html',{})

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
