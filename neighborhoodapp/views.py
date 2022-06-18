from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'all_templates/index.html')

def signup(request):
    return render(request, 'all_templates/signup.html')

def signin(request):
    return render(request, 'all_templates/signin.html')

def logout(request):
    return redirect('signin')

def search(request):
    return render(request, 'all_templates/search.html')

def profile(request):
    return render(request, 'all_templates/profile.html')