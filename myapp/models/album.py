# myapp/models/album.py
from django.db import models
from .user import User  # User modelini import ediyoruz

class Album(models.Model):
    user = models.ForeignKey(User, related_name='albums', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
