"""
    Se registra la clase de UserProfile en el panel de administracion
"""
from users.models import UserProfile
from django.contrib import admin

admin.site.register(UserProfile)