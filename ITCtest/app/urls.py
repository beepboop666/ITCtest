# -*- coding: utf-8 -*-
# Created by Danil Sviridov

from django.urls import path
from django.views.generic import TemplateView
from . import view

urlpatterns = [
    path('map/', TemplateView.as_view(template_name='main.html'), name='check2'),
    path('', view.check, name='check'),
    path('api/', view.sensors, name='main')
]