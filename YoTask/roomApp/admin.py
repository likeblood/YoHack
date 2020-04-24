from django.contrib import admin
from .models import Task, Room


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['author']


@admin.register(Room)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['room_name']
