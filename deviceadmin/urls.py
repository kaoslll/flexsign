from django.urls import path
from . import views


"""
Import: 
        + Django-Funktion path
        + alle views von deviceadmin
        
Beschreibung:
        + Urlpattern für die Administration der Endgeräte
"""


urlpatterns = [
    path('', views.helloworld, name='helloworld'),
]

