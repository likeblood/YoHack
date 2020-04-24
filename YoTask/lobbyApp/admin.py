from django.contrib import admin
from .models import Lobby


@admin.register(Lobby)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['lobby_name']
