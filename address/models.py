from django.db import models
from user.models import User
# from ... import User

# Create your models here.

class Address(models.Model):
    name = models.CharField(blank=False, max_length=70)
    longitude = models.DecimalField(blank=False, max_digits=20, decimal_places=17)
    latitude = models.DecimalField(blank=False, max_digits=20, decimal_places=17)
    start = models.BooleanField(default=False)
    end = models.BooleanField(default=False)
    stop = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)