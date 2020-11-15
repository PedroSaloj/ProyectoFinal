"""
    Pantalla de login
"""

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render, redirect

def logon(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            userSession = authenticate(request, username = username, password = password)
            #user = User.objects.create_user(username, '', password=password)
            if userSession:
                login(request, userSession)
                return redirect("homepage")
            else:
                return render(request, 'login.html', {'error' : "Invalid username or password"})
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            age = request.POST["age"]
            if password != password2:
                return render(request, 'register.html', {'error' : "Las contraseñas son diferentes"})
            user = User.objects.create_user(username, email=email, password=password)
            user.age = age
            user.save()
            return render(request, 'login.html', {'error' : "Please, login"})

    return render(request,'register.html')
    return render(request,'edit.html')

def logout_view(request):
    logout(request)
    return redirect("logon")