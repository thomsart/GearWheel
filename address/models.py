from django.db import models

from ... import User

# Create your models here.

class Address(models.Model):
    name = models.CharField(blanck=False, max_length=70)
    longitude = models.DecimalField(blanck=False, max_digits=20, decimal_places=17)
    latitude = models.DecimalField(blanck=False, max_digits=20, decimal_places=17)
    start = models.BooleanField(default=False)
    end = models.BooleanField(default=False)
    stop = models.BooleanField(default=False)
    user = models.ForeignKey(User)