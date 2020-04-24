from django.db import models
from usersApp.models import User


class Lobby(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lobby_creator")
    users = models.ManyToManyField(User, related_name="lobby_users")

    lobby_name = models.CharField(max_length=30)
    lobby_description = models.TextField()
