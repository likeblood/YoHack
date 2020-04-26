from django.db import models
from usersApp.models import User


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    asignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="asignee")

    room_id = models.IntegerField()
    task_title = models.CharField(max_length=40)
    task_description = models.TextField()
    date = models.DateTimeField()
    is_done = models.BooleanField()


class Room(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name="room_creator")

    users = models.ManyToManyField(User)
    tasks = models.ManyToManyField(Task)

    room_name = models.CharField(max_length=30)
    room_description = models.TextField()
    is_private = models.BooleanField()
    room_password = models.TextField()

    def __str__(self):
        return self.room_name


class Lobby(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lobby_creator")
    users = models.ManyToManyField(User, related_name="lobby_users")
    rooms = models.ManyToManyField(Room)

    lobby_name = models.CharField(max_length=30)
    lobby_password = models.TextField()

    def __str__(self):
        return self.lobby_name

