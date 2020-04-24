from django.db import models
# from lobbyApp.models import Lobby
from usersApp.models import User


class Room(models.Model):
    # lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    room_name = models.CharField(max_length=15)

    def __str__(self):
        return room_name


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    task_title = models.CharField(max_length=40)
    task_description = models.TextField()
    date = models.DateTimeField()
    is_done = models.BooleanField()
