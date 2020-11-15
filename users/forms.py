from django import forms
from django.forms import ModelForm
from users.models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['marca','modelo','codigo','descripcion','serie','estado']
