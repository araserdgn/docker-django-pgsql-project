# myapp/models/post.py
from django.db import models
from .user import User  # User modelini import ediyoruz

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
