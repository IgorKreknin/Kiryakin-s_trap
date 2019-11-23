from django.shortcuts import render
from django.http import HttpResponse
from .models import ParkingSlot, Camera, Path
import json
import requests

def parseSlots():
    r = requests.get('https://apidata.mos.ru/v1/datasets/916/rows/?api_key=58ff41c0abee7d2fe80731ef9f37d833')
    for p in r.json():
        data = ParkingSlot(
        globalId = p['Cells']['global_id'],
        name = p['Cells']['Name'],
        admArea = p['Cells']['AdmArea'],
        district = p['Cells']['District'],
        address = p['Cells']['Address'],
        departamentalAffilation = p['Cells']['DepartamentalAffiliation'],
        capacity = p['Cells']['Capacity'],
        objectOperOrgName = p['Cells']['ObjectOperOrgName'],
        coordinates = json.dumps(p['Cells']['geoData']['coordinates'])
        )
        data.save()

def parseMassCameras():
    r = requests.get('https://apidata.mos.ru/v1/datasets/2386/rows/?api_key=58ff41c0abee7d2fe80731ef9f37d833')
    for p in r.json():
        data = Camera(
        globalId = p['Cells']['global_id'],
        name = p['Cells']['ID'],
        district = p['Cells']['District'],
        address = p['Cells']['Address'],
        ovdAddress = p['Cells']['Address'],
        admArea = p['Cells']['AdmArea'],
        coordinates = json.dumps(p['Cells']['geoData']['coordinates'])
        )
        data.save()

def parceYardCameras():
    count = requests.get('https://apidata.mos.ru/v1/datasets/1498/count/?api_key=58ff41c0abee7d2fe80731ef9f37d833').json()
    skip = 0
    while (skip <= count):
        r = requests.get('https://apidata.mos.ru/v1/datasets/1498/rows/?api_key=58ff41c0abee7d2fe80731ef9f37d833&$skip=%d&$top=500'
        % (skip))
        print(skip)
        for p in r.json():
            data = Camera(
            globalId = p['Cells']['global_id'],
            name = p['Cells']['ID'],
            district = p['Cells']['District'],
            address = p['Cells']['Address'],
            ovdAddress = p['Cells']['Address'],
            admArea = p['Cells']['AdmArea'],
            coordinates = json.dumps(p['Cells']['geoData']['coordinates'])
            )
            data.save()
        skip += 500


def parcePath():
    r = requests.get('https://apidata.mos.ru/v1/datasets/897/rows/?api_key=58ff41c0abee7d2fe80731ef9f37d833')
    for p in r.json():
        data = Path(
        globalId = p['Cells']['global_id'],
        name = p['Cells']['Name'],
        location = p['Cells']['Location'],
        coordinates = json.dumps(p['Cells']['geoData']['coordinates'])
        )
        data.save()

def index(request):
    if (len(ParkingSlot.objects.all()) == 0):
        parseSlots()
    if (len(Camera.objects.all()) == 0):
        parseMassCameras()
        parceYardCameras()
    if (len(Path.objects.all()) == 0):
        parcePath()
    return HttpResponse('Working')
