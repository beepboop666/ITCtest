# -*- coding: utf-8 -*-
# Created by Danil Sviridov

from djgeojson.fields import PointField
from django.db import models


class WeatherSensor(models.Model):

    pm25 = models.FloatField()
    pm10 = models.FloatField()
    hum = models.FloatField()
    press = models.FloatField()
    temp = models.FloatField()
    latest = models.BooleanField()
    geom = PointField()
