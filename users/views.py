"""
    Pantalla de login
"""

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Ticket
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