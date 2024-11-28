# myapp/models/company.py
from django.db import models
from .user import User  # User modelini import ediyoruz

class Company(models.Model):
    name = models.CharField(max_length=200)
    catch_phrase = models.CharField(max_length=200)
    bs = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='company', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
