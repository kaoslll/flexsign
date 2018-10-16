from django.contrib import admin
from .models import Room, Event


""" 
Hiermit wird direkter Datenbankzugriff über die Admin-Oberfläche ermöglicht
"""
admin.site.register(Room)
admin.site.register(Event)
