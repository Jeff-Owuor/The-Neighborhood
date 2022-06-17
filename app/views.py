from django.shortcuts import render,redirect
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .forms import RegisterForm

# Create your views here.


def index(request):
    return render(request,'app/index.html',{})

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, 'registration/register.html', {"form":form})