from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'login be successful')
            return redirect('login')
        else:
            messages.success(request, 'we have trouble! please try again later!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken!')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Account created!')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match!')
        return redirect('login')
    else:
        return render(request, 'login.html')

def Logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')


