from django.shortcuts import render,redirect
from .forms import RegisterForm

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