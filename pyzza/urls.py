"""
    pyzza URL Configuration
"""
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from pyzza import views as general
from users import views as users

urlpatterns = [
    path('', general.homepage, name = "homepage"),
    path('admin/', admin.site.urls, name = "administration"),
    path('login/', users.logon, name = "logon"),
    path('register/', users.signup, name = "register"),
    path('logout/', users.logout_view, name = "logout"),
    path('users/edit/<int:id>', users.signup , name = "user_edit"),
    path('tickets/', users.ticket_list, name="ticketlist"),
    path('tickets/edit/', users.ticket_edit, name="ticket_edit"),
    path('tickets/edit/<int:id>', users.ticket_edit, name="ticket_edit")
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)