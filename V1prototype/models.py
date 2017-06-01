from __future__ import unicode_literals

from django.db import models

# Create your models here.

class tide(models.Model):
    parameterName = models.CharField(max_length=200)
    value = models.IntegerField()
    unit = models.CharField(max_length=50)
    time = models.DateTimeField(default=1)
    locationName = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    lon = models.DecimalField(max_digits=12, decimal_places=4, default=0)

class chlorosity(models.Model):
    parameterName = models.CharField(max_length=200)
    value = models.IntegerField()
    unit = models.CharField(max_length=50)
    time = models.DateTimeField(default=1)
    locationName = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    lon = models.DecimalField(max_digits=12, decimal_places=4, default=0)



