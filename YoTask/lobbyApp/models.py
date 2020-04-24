from django.db import models

# waiting for User model to import it


class Lobby(models.Model):
	creater = models.ForeignKey(User, on_delete=models.CASCADE)

	lobby_name = models.CharField(max_length = 30)
	lobby_description = models.TextField()
