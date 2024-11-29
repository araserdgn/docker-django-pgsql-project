# myapp/models/company.py
from django.db import models
from .user import User  # User modelini import ediyoruz

class Company(models.Model):
    name = models.CharField(max_length=200)
    catch_phrase = models.CharField(max_length=200)
    bs = models.CharField(max_length=200)
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='company')

    def __str__(self):
        return self.name
