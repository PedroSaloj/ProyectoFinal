"""
    Archivo general de vistas del proyecto
    Login / HomePage
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def homepage(request):
    users = User.objects.order_by('-username')
    return render(request, 'index.html', {'users': users})



def lista(request):
    users = User.objects.order_by('-username')
    #users = UserProfile.objects.all()
    return render(request, 'index.html', {'users': users})

def edit(request):
    users = User.objects.order_by('-username')
    #users = UserProfile.objects.all()
    return render(request, 'edit.html', {'users': users})