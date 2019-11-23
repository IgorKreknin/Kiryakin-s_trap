from django.conf import settings
from django.db import models
from .config import api_config
import json
from .arithmetics.geoDistance import isCovered

class ParkingSlot(models.Model):
    globalId = models.IntegerField(default = 0)
    name = models.TextField()
    admArea = models.TextField()
    district = models.TextField()
    address = models.TextField()
    departamentalAffilation = models.TextField()
    capacity = models.IntegerField(default = 0)
    objectOperOrgName = models.TextField()
    coordinates = models.TextField()
    cameras = models.IntegerField(default = 0)


class Camera(models.Model):
    globalId = models.IntegerField(default = 0)
    name = models.TextField()
    district = models.TextField()
    address = models.TextField()
    ovdAddress = models.TextField()
    admArea = models.TextField()
    coordinates = models.TextField()
    coveredSlots = models.TextField(blank = True)

class Path(models.Model):
    globalId = models.IntegerField(default = 0)
    name = models.TextField()
    location = models.TextField()
    coordinates = models.TextField()

class Kiosk(models.Model):
    globalId = models.IntegerField(default = 0)
