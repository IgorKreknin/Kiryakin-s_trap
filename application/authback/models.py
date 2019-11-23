from django.conf import settings
from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 30)
    phone = models.IntegerField()
    login = models.CharField(max_length = 20)
    passw = models.CharField(max_length = 30)
    email = models.EmailField()
    bicycle = models.TextField(blank = True)
    premium = models.BooleanField(default = False)

    def addBicycle(bicycles):
        self.bicycle = json.dumps({
        'genericId': bicycles.genericId,
        'isStolen': bicycles.isStolen,
        })
        bicycles.owner = self

class Bicycle(models.Model):
    genericId = models.IntegerField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = '+')
    isStolen = models.BooleanField(default = False)
