# -*- coding: utf-8 -*-
# Created by Danil Sviridov

import json
from math import floor
from django.http import HttpResponse, JsonResponse
from .models import WeatherSensor


def coloring(type, val):
    if type == 'pm25':
        if 0 <= val < 76:
            return 1
        elif 76 <= val <= 150:
            return 2
        else:
            return 3
    elif type == 'pm10':
        if 0 <= val < 76:
            return 1
        elif 76 <= val <= 150:
            return 2
        else:
            return 3
    elif type == 'hum':
        if 30 <= val <= 50:
            return 1
        elif 25 <= val < 30 or 50 < val <= 70:
            return 2
        else:
            return 3
    elif type == 'press':
        if 747 < val < 749:
            return 1
        elif 738 <= val <= 747 or 749 <= val <= 758:
            return 2
        else:
            return 3
    elif type == 'temp':
        if 14 <= val <= 24:
            return 1
        elif 6 <= val < 14 or 24 < val <= 30:
            return 2
        else:
            return 3


def check(request):
    return HttpResponse("Check")


def sensors(request):
    d = json.loads(request.body)
    pm25 = d.get('pm25')
    pm10 = d.get('pm10')
    temp = d.get('temp')
    hum = d.get('hum')
    press = d.get('press')
    sens_raw_data = WeatherSensor.objects.raw('SELECT * FROM sensors WHERE latest')
    sens_data = []
    for i in sens_raw_data:
        sum = 0.0
        cnt = 0
        if pm25 == 1:
            sum += coloring('pm25', i.pm25)
            cnt += 1
        if pm10 == 1:
            sum += coloring('pm10', i.pm10)
            cnt += 1
        if temp == 1:
            sum += coloring('temp', i.temp)
            cnt += 1
        if press == 1:
            sum += coloring('press', i.press)
            cnt += 1
        if hum == 1:
            sum += coloring('hum', i.hum)
            cnt += 1
        sum = floor(sum / cnt)
        sens_data.append({
            'degrees': i.geom,
            'color': int(sum),
        })
    response = {
        'sensors': sens_data,
        'count': len(sens_data)
    }
    return JsonResponse(response)


def add_new_sensor_data():
    pass
