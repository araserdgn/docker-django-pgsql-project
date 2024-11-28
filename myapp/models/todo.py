# myapp/models/todo.py
from django.db import models
from .user import User  # User modelini import ediyoruz

class Todo(models.Model):
    user = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
