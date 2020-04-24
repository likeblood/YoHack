# from django.db import models
# from roomApp.models import Room
#
# # waiting for User model to import it
#
#
# class Lobby(models.Model):
# 	creator = models.ForeignKey(User, on_delete=models.CASCADE)
# 	users = models.ManyToManyField(User)
# 	rooms = models.ManyToManyField(Room)
#
# 	lobby_name = models.CharField(max_length = 30)
# 	lobby_description = models.TextField()
