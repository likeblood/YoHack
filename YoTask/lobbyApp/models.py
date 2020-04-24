from django.db import models
# from roomApp.models import Room
from usersApp.models import User

#
# class Lobby(models.Model):
#     creator = models.ForeignKey(User, on_delete=models.CASCADE)
#     users = models.ManyToManyField(User)
#     rooms = models.ManyToManyField(Room)
#
#     lobby_name = models.CharField(max_length=30)
#     lobby_description = models.TextField()
