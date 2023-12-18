from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.create(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('home')

    return render(request, "home.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('home')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')