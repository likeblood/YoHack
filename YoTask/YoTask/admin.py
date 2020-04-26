from django.contrib import admin
from .models import Task, Room
from .models import Lobby


@admin.register(Lobby)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'lobby_name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'author']


@admin.register(Room)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'room_name']
