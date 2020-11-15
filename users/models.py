"""
    Modelo Proxy para usuarios de nuestro sistema
"""

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, blank=True)
    userImage = models.ImageField(
        upload_to = "users/pictures",
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Ticket(models.Model):
    INGRESADO = 'I'
    ENPROCESO = 'P'
    REPARADO = 'R'
    ENTREGADO = 'E'
    OPCIONES_ESTADO = [
        (INGRESADO,'Ingresado'),
        (ENPROCESO, 'En Proceso'),
        (REPARADO, 'Reparado'),
        (ENTREGADO, 'Entregado')
    ]
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    codigo = models.CharField(max_length=25)
    descripcion = models.TextField(max_length = 1000)
    serie = models.CharField(max_length=25)
    estado = models.CharField(
        max_length=1,
        choices = OPCIONES_ESTADO,
        default = INGRESADO
    )
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def is_upperclass(self):
        return True