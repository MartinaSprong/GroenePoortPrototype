from django.shortcuts import render, redirect
from V1prototype.models import tide 
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json
import urllib2
from django.http import HttpResponse
import os
import sys
import numpy
import datetime
import time

import logging
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def index(request):
    #tide.objects.filter(locationName="Eemshaven")
    #tide.objects.order_by('id')
    context = dict()
    context['tides'] = tide.objects.all()
    return render(request,'V1prototype/index.html', context)

def graphView(request):
    return render(request, 'V1prototype/graph.html')
    
def jsonGetTide(object):
    #  download and de-serialize json
     tideUrl = json.load(urllib2.urlopen('https://waterinfo.rws.nl/api/point/latestmeasurements?parameterid=waterhoogte-t-o-v-nap '))
     tideValues = tideUrl['features']
     for tideValue in tideValues:
         tideMeasurements = tideValue['properties']['measurements']
         for tideValueSecond in tideMeasurements:
             latestValue = tideValueSecond['dateTime']
    #      correctTime = (datetime.datetime.fromtimestamp(int(tideTime)).strftime('%Y-%m-%d %H:%M:%S'))
             t1 = tide.objects.update_or_create(parameterName=tideValueSecond['parameterId'], 
                                                    value=tideValueSecond['latestValue'], 
                                                    unit=tideValueSecond['unitCode'],
                                                    time=tideValueSecond['dateTime'], 
                                                    locationName=tideValue['properties']['name'],
                                                    lat=tideValue['geometry']['coordinates'][0],
                                                    lon=tideValue['geometry']['coordinates'][1])
     log.debug("Entering debug mode")
     log.info("Hey there it works!!")
     log.debug("Checking for git user") 
     print(t1)  
     return HttpResponse()


    