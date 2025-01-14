from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from events.EmailBackEnd import EmailBackEnd
from .models import Guest


def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # for checking email
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'email already exist')
            return redirect('register')
        # for checking username
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'username already exists')
            return redirect('register')
        # for saving sing up details
        user = User(email=email, username=username)
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request, 'registration/signup.html')


def DOLOGIN(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = EmailBackEnd.authenticate(request, username=email, password=password)
        if user != None:
            login(request, user)
            return redirect('event_list')
        else:
            messages.error(request, 'Email and Password Are Invalid !')
            return redirect('login')
    return render(request, 'registration/login.html')


def GUEST_LOGIN(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        guest_data = Guest(name=name, email=email, mobile=mobile)
        guest_data.save()
        messages.success(request, 'Guest logged in successfully!')
        return redirect('guest_event_list')
    return render(request, 'registration/guest_login.html')


def LOGIN_REQUIRED(request):
    return render(request, 'guest/guest_login.html')


def DOLOGOUT(request):
    logout(request)
    return render(request, 'main/home.html')
