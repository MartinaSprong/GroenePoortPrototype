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
import math

import logging
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def utmToLatLng(zone, easting, northing, northernHemisphere=True):
    if not northernHemisphere:
        northing = 10000000 - northing

    a = 6378137
    e = 0.081819191
    e1sq = 0.006739497
    k0 = 0.9996

    arc = northing / k0
    mu = arc / (a * (1 - math.pow(e, 2) / 4.0 - 3 *
                     math.pow(e, 4) / 64.0 - 5 * math.pow(e, 6) / 256.0))

    ei = (1 - math.pow((1 - e * e), (1 / 2.0))) / \
        (1 + math.pow((1 - e * e), (1 / 2.0)))

    ca = 3 * ei / 2 - 27 * math.pow(ei, 3) / 32.0

    cb = 21 * math.pow(ei, 2) / 16 - 55 * math.pow(ei, 4) / 32
    cc = 151 * math.pow(ei, 3) / 96
    cd = 1097 * math.pow(ei, 4) / 512
    phi1 = mu + ca * math.sin(2 * mu) + cb * math.sin(4 * mu) + \
        cc * math.sin(6 * mu) + cd * math.sin(8 * mu)

    n0 = a / math.pow((1 - math.pow((e * math.sin(phi1)), 2)), (1 / 2.0))

    r0 = a * (1 - e * e) / \
        math.pow((1 - math.pow((e * math.sin(phi1)), 2)), (3 / 2.0))
    fact1 = n0 * math.tan(phi1) / r0

    _a1 = 500000 - easting
    dd0 = _a1 / (n0 * k0)
    fact2 = dd0 * dd0 / 2

    t0 = math.pow(math.tan(phi1), 2)
    Q0 = e1sq * math.pow(math.cos(phi1), 2)
    fact3 = (5 + 3 * t0 + 10 * Q0 - 4 * Q0 * Q0 -
             9 * e1sq) * math.pow(dd0, 4) / 24

    fact4 = (61 + 90 * t0 + 298 * Q0 + 45 * t0 * t0 - 252 *
             e1sq - 3 * Q0 * Q0) * math.pow(dd0, 6) / 720

    lof1 = _a1 / (n0 * k0)
    lof2 = (1 + 2 * t0 + Q0) * math.pow(dd0, 3) / 6.0
    lof3 = (5 - 2 * Q0 + 28 * t0 - 3 * math.pow(Q0, 2) + 8 *
            e1sq + 24 * math.pow(t0, 2)) * math.pow(dd0, 5) / 120
    _a2 = (lof1 - lof2 + lof3) / math.cos(phi1)
    _a3 = _a2 * 180 / math.pi

    latitude = 180 * (phi1 - fact1 * (fact2 + fact3 + fact4)) / math.pi

    if not northernHemisphere:
        latitude = -latitude

    longitude = ((zone > 0) and (6 * zone - 183.0) or 3.0) - _a3

    return (latitude, longitude)


def index(request):
    # tide.objects.filter(locationName="Eemshaven")
    # tide.objects.order_by('id')
    context = dict()
    context['tides'] = tide.objects.all()
    return render(request, 'V1prototype/index.html', context)


def graphView(request, oid):
    contextGraph = dict()
    contextGraph['tidesGraph'] = tide.objects.filter(id=oid).first()
    return render(request, 'V1prototype/graph.html', contextGraph)

def jsonGetTide(object):
    #  download and de-serialize json
    tideUrl = json.load(urllib2.urlopen(
        'https://waterinfo.rws.nl/api/point/latestmeasurements?parameterid=waterhoogte-t-o-v-nap '))
    tideValues = tideUrl['features']
    for tideValue in tideValues:
        tideMeasurements = tideValue['properties']['measurements']
        convertCoordinates = utmToLatLng(31, tideValue['geometry']['coordinates'][0],
                                         tideValue['geometry']['coordinates'][1],
                                         northernHemisphere=True)
        for tideValueSecond in tideMeasurements:
            latestValue = tideValueSecond['dateTime']
    #      correctTime = (datetime.datetime.fromtimestamp(int(tideTime)).strftime('%Y-%m-%d %H:%M:%S'))
            t1 = tide.objects.update_or_create(parameterName=tideValueSecond['parameterId'],
                                               value=tideValueSecond['latestValue'],
                                               unit=tideValueSecond['unitCode'],
                                               time=tideValueSecond['dateTime'],
                                               locationName=tideValue['properties']['name'],
                                               lat=convertCoordinates[0],
                                               lon=convertCoordinates[1])
    log.debug("Entering debug mode")
    log.info("Hey there it works!!")
    log.debug("Checking for git user")
    print t1
    return HttpResponse()
