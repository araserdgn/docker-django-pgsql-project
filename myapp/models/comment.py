# myapp/models/comment.py
from django.db import models
from .post import Post  # Post modelini import ediyoruz

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"
