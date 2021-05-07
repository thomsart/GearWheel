from django.db import models
from bestway.models import User
# from ... import User

# Create your models here.

class Address(models.Model):
    name = models.CharField(blank=False, max_length=70)
    longitude = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    start = models.BooleanField(default=False)
    end = models.BooleanField(default=False)
    stop = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)