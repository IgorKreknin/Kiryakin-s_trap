from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User, Bicycle
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    dict = json.loads(request.body.decode('utf-8'))
    if (checkRequirements(argDict)):
        if (dict['type'] == 'register'):
            result = createUser(dict)
        if (dict['type'] == 'auth'):
            result = logInUser(dict)
    if (result["Result"]):
        return JsonResponse(result)
    return JsonResponse({"Result": False})

def checkRequirements(argDict):
    userlist = User.objects.filter(login = argDict['login']
    or email = argDictp['email'])
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
    if (str(int(argDict['phone'])) != argDict['phone']):
        return False
    if (argDict['email'] == ''):
        return False
    if (not re.fullmatch('[^@]+@[^@]+\.[^@]+', argDict['email'])):
        return False
    return True

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
    return {"Result": True, "User": argDict}

def logInUser(argDict):
    return {"Result": True, "User": argDict}
