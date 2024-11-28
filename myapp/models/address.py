from django.db import models
from .user import User

class Address(models.Model):
    street = models.CharField(max_length=200)
    suite = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    geo_lat = models.DecimalField(max_digits=10, decimal_places=6)
    geo_lng = models.DecimalField(max_digits=10, decimal_places=6)
    user = models.ForeignKey(User, related_name='address', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street}, {self.city}"