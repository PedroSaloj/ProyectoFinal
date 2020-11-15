"""
    Pantalla de login
"""

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Ticket, UserProfile
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import TicketForm

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

def signup(request, id=None):
    if request.method == 'POST':
        if(id != 0):
            user = User.objects.get(id=id)
            profile = UserProfile.objects.get(user=user)
            user.username = request.POST['username']
            user.email = request.POST['email']
            if request.POST['password'] != request.POST['password2']:
                return render(request, 'register.html', {'error' : "Las contraseñas son diferentes"})
            if request.POST['password'] != '':
                user.set_password(request.POST['password'])
            user.save()
            profile.age = request.POST["age"]
            if request.FILES:
                profile.userImage = request.FILES['image']
            profile.save()
            return redirect('homepage')
        else:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            age = request.POST["age"]
            if password != password2:
                return render(request, 'register.html', {'error' : "Las contraseñas son diferentes"})
            user = User.objects.create_user(username, email=email, password=password)
            userprofile = UserProfile(
                user=user,
                age=request.POST['age'],
                userImage = request.FILES['image']
            )
            userprofile.save()
            return render(request, 'login.html', {'error' : "Please, login"})
    else:
        if(id is not None):
            user = User.objects.get(id=id)
            profile = UserProfile.objects.get(user=user)
            data = {
            'username': user.username,
            'email': user.email,
            'age': profile.age,
            'id': id
            }
        else:
            data = {
                'id': 0
            }
        return render(request,'edit.html',{'user':data})

def logout_view(request):
    logout(request)
    return redirect("logon")

def ticket_list(request):
    tickets = Ticket.objects.order_by('-id')
    return render(request, 'Tickets/index.html', {'tickets': tickets})

def ticket_edit(request, id=None):
    if request.method == "POST":
        if(id != 0):
            ticket = Ticket.objects.get(id=id)
        else:
            ticket = Ticket()
        
        ticket.marca=request.POST['marca']
        ticket.modelo = request.POST['modelo']
        ticket.serie = request.POST['serie']
        ticket.codigo = request.POST['codigo']
        ticket.estado = request.POST['estado']
        ticket.descripcion = request.POST['descripcion']
        
        
        ticket.save()
        return redirect('ticketlist')
    else:
        if(id is not None):
            ticket = Ticket.objects.get(id=id)
        else:
            ticket = Ticket()
            id=0
        data = {
            'marca': ticket.marca,
            'modelo': ticket.modelo,
            'serie': ticket.serie,
            'codigo': ticket.codigo,
            'estado': ticket.estado,
            'descripcion': ticket.descripcion
        }
        form = TicketForm(data)
        return render(request,'Tickets/edit.html',{'form':form, 'id':id})