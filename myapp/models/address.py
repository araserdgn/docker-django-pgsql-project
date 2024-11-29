from django.db import models
from .user import User

class Address(models.Model):
    street = models.CharField(max_length=200)
    suite = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    geo_lat = models.DecimalField(max_digits=20, decimal_places=6)
    geo_lng = models.DecimalField(max_digits=20, decimal_places=6)
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='address')

    def __str__(self):
        return f"{self.street}, {self.city}"