from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ParkingSlot, Camera, Path, Kiosk
from .config import api_config
from .config import valid_kiosk_specs
from .arithmetics.geoDistance import isCovered, geoDistance
import json
import requests
from django.views.decorators.csrf import csrf_exempt


def parseSlots():
    r = requests.get('https://apidata.mos.ru/v1/datasets/%d/rows/?api_key=%s'
    % (api_config['id_parkingSlots'], api_config['api_key']))
    cameras = Camera.objects.all()
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
        for i in cameras:
            if(geoDistance(json.loads(data.coordinates), json.loads(i.coordinates)) <= api_config['standart_range']):
                data.cameras += 1
        data.save()

def parseMassCameras():
    r = requests.get('https://apidata.mos.ru/v1/datasets/%d/rows/?api_key=%s'
    % (api_config['id_massCameras'], api_config['api_key']))
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
    count = requests.get('https://apidata.mos.ru/v1/datasets/%d/count/?api_key=%s'
    % (api_config['id_yardCameras'], api_config['api_key'])).json()
    skip = 0
    while (skip <= count):
        r = requests.get('https://apidata.mos.ru/v1/datasets/%d/rows/?api_key=%s&$skip=%d&$top=500'
        % (api_config['id_yardCameras'], api_config['api_key'], skip))
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


def parcePaths():
    r = requests.get('https://apidata.mos.ru/v1/datasets/%d/rows/?api_key=%s'
    % (api_config['id_paths'], api_config['api_key']))
    for p in r.json():
        data = Path(
        globalId = p['Cells']['global_id'],
        name = p['Cells']['Name'],
        location = p['Cells']['Location'],
        coordinates = json.dumps(p['Cells']['geoData']['coordinates'])
        )
        data.save()


def parceKiosks(kioskId):
    r = requests.get('https://apidata.mos.ru/v1/datasets/%d/rows/?api_key=%s'
    % (kioskId, api_config['api_key']))
    for p in r.json():
        if (p['Cells']['ContractStatus'] == 'действует') and (p['Cells']['Specialization'][0] in valid_kiosk_specs):
            print(1)
            data = Kiosk(
                globalId = p['Cells']['global_id'],
                name = p['Cells']['Name'],
                admArea = p['Cells']['AdmArea'],
                district = p['Cells']['District'],
                address = p['Cells']['Address'],
                objectType = p['Cells']['ObjectType'],
                nameOfBusinessEntity = p['Cells']['NameOfBusinessEntity'],
                coordinates = json.dumps(p['Cells']['geoData']['coordinates'])
            )
            data.save()

def getNearest(coordList):
    parkingStations = ParkingSlot.objects.all()
    result = []
    radius = 50
    while (len(result) == 0):
        for i in parkingStations:
            if (geoDistace(coordList, json.loads(i['coordinates'])) <= radius):
                result.append(i['globalId'])
        if (radius == 300 and len(result) == 0):
            return {"Result": False}
        radius += 50
    return {"Result": True, "PointIds": result}

def addUserRating(addId, newRating):
    parkingStations = ParkingSlot.objects.filter(globalId = addId)
    parkingStations.calculateUserRating(newRating)

@csrf_exempt
def index(request):
    if (len(Camera.objects.all()) == 0):
        parseMassCameras()
        parceYardCameras()
        return HttpResponse('Parced Cameras')
    if (len(ParkingSlot.objects.all()) == 0):
        parseSlots()
        return HttpResponse('Parced Parking Slots')
    if (len(Path.objects.all()) == 0):
        parcePaths()
        return HttpResponse('Parced Cycle Paths')
    if (len(Kiosk.objects.all()) == 0):
        parceKiosks(api_config['id_kiosks'])
        parceKiosks(api_config['id_kiosks_reserves'])
        parceKiosks(api_config['id_kiosks_parks'])
        return HttpResponse('Parced Kiosks')
    req = json.loads(request.body.decode('utf-8'))
    if (req['RequestType'] == 'giveData'):
        returnList = []
        for i in ParkingSlot.objects.all():
            returnList.append({
            'globalId': i.globalId,
            'name': i.name,
            'coordinates': i.coordinates,
            'userRating': i.userRating.currentRating,
            })
        return JsonResponse(returnList, safe = False)
    if (req['RequestType'] == 'giveNearest'):
        return JsonResponse(getNearest(req['Point']), safe = False)
    return HttpResponse('Working')
