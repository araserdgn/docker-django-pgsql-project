# myapp/models/photo.py
from django.db import models
from .album import Album  # Album modelini import ediyoruz

class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title
