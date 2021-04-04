from django.contrib import admin
from .models import Service, Position, Team

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position', 'active', 'modified')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'icons', 'active', 'modified')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'active','modified')