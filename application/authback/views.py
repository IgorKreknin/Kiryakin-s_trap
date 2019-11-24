from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User, Bicycle
import json
import re
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if (request.method == 'GET'):
        return JsonResponse({"Result": False})
    dict = json.loads(request.body.decode('utf-8'))
    print(dict)
    result = {"Result": False}
    if (checkRequirementsReg(dict)):
        if (dict['action'] == 'register'):
            result = createUser(dict)
    if (checkRequirementsLog(dict)):
        if (dict['action'] == 'auth'):
            result = logInUser(dict)
    if (result["Result"]):
        return JsonResponse(result)
    return JsonResponse({"Result": False})

def checkRequirementsReg(argDict):
    userloginlist = User.objects.filter(login = argDict['login'])
    useremaillist = User.objects.filter(email = argDict['email'])
    if (len(userloginlist) != 0 or len(useremaillist) != 0):
        return False
    if (argDict['login'] == ''):
        return False
    if (argDict['password'] == ''):
        return False
    if (argDict['password'] != argDict['password_repeat']):
        return False
    if (argDict['name'] == ''):
        return False
    if (argDict['lastname'] == ''):
        return False
    if (argDict['phone'] == ''):
        return False
    if (len(argDict['phone']) != 12):
        return False
    if (argDict['phone'][0] != '+'):
        return False
    if (not bool(re.match('^(\d{11})$', argDict['phone'][1:]))):
        return False
    if (argDict['email'] == ''):
        return False
    if (not bool(re.match('[^@]+@[^@]+\.[^@]+', argDict['email']))):
        return False
    return True

def checkRequirementsLog(argDict):
    userloginlist = User.objects.filter(login = argDict['login'])
    print(userloginlist)
    if (len(userloginlist) == 0):
        return False
    if (argDict['login'] == ''):
        return False
    if (argDict['password'] == ''):
        return False
    if (argDict['password'] != userloginlist['passw']):
        return False


def createUser(argDict):
    data = User(
    name = argDict['name'],
    surname = argDict['lastname'],
    phone = int(argDict['phone'][1:]),
    login = argDict['login'],
    passw = argDict['password'],
    email = argDict['email']
    )
    data.save()
    print('Person registered')
    return {"Result": True, "User": argDict}

def logInUser(argDict):
    print('Log In success')
    return {"Result": True, "User": argDict}
