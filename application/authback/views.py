from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Bicycle

def index(request):
    return HttpResponse('heh boi l l l l l l lallalalala')

"""
def createUser(request):
    data = User(
    name = ,
    surname = ,
    phone = ,
    login = ,
    passw = ,
    email = ,
    data = ,
    )
    data.save()
"""
