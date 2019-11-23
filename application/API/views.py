from django.shortcuts import render
from django.http import HttpResponse
from .models import ParkingSlot, Camera, Path
from .config import api_config
import json
import requests

def parseSlots():
    r = requests.get('https://apidata.mos.ru/v1/datasets/%d/rows/?api_key=%d'
    % (api_config['id_parkingSlots'], api_config['api_key']))
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
    r = requests.get('https://apidata.mos.ru/v1/datasets/%d/rows/?api_key=%d'
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
        data.calculateCameras()
        data.save()

def parceYardCameras():
    count = requests.get('https://apidata.mos.ru/v1/datasets/%d/count/?api_key=%d'
    % (api_config['id_yardCameras'], api_config['api_key'])).json()
    skip = 0
    while (skip <= count):
        r = requests.get('https://apidata.mos.ru/v1/datasets/%d/rows/?api_key=%d&$skip=%d&$top=500'
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
    r = requests.get('https://apidata.mos.ru/v1/datasets/%d/rows/?api_key=%d'
    % (api_config['id_paths'], api_config['api_key']))
    for p in r.json():
        data = Path(
        globalId = p['Cells']['global_id'],
        name = p['Cells']['Name'],
        location = p['Cells']['Location'],
        coordinates = json.dumps(p['Cells']['geoData']['coordinates'])
        )
        data.save()


def parceKiosks():
   r = requests.get('https://apidata.mos.ru/v1/datasets/%d/rows/?api_key=%d'
    % (api_config['id_kiosks'], api_config['api_key']))
    for p in r.json():
        if (p['Cells']['Contract'] == 'действует') and (p['Cells']['Specialisation'] in valid_kiosk_specs):
            data = Kiosk(
                globalId = p['Cells']['global_id'],         #не уверен в формате "исходных данных"
                name = p['Cells']['Name'],
                location = p['Cells']['Location'],
                coordinates = json.dumps(p['Cells']['geoData']['coordinates'])
                specialisation = p['Cells']['Specialisation']                       #мб понадобится
            )
            data.save()


def parseKiosksPrefect():                                       #мб можно будет забить всё в один parceKiosks, но мы готовы к различию форматов
    r = requests.get('https://apidata.mos.ru/v1/datasets/%d/rows/?api_key=%d'
    % (api_config['id_kiosks_prefect'], api_config['api_key']))
    for p in r.json():
        if (p['Cells']['Contract'] == 'действует') and (p['Cells']['Specialisation'] in valid_kiosk_specs):
            data = Kiosk(
                globalId = p['Cells']['global_id'],         #не уверен в формате "исходных данных"
                name = p['Cells']['Name'],
                location = p['Cells']['Location'],
                coordinates = json.dumps(p['Cells']['geoData']['coordinates'])
                specialisation = p['Cells']['Specialisation']                       #мб понадобится
            )
            data.save()


def index(request):
    if (len(Camera.objects.all()) == 0):
        parseMassCameras()
        parceYardCameras()
    if (len(ParkingSlot.objects.all()) == 0):
        parseSlots()
    if (len(Path.objects.all()) == 0):
        parcePaths()
    return HttpResponse('Working')
