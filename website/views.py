from django.shortcuts import render
from http import client
from urllib.parse import urlparse
import json
# Create your views here.

ATOM_LOC = "10.100.148.152"
API_KEY = '799cbb5aae706a3a'

def index(request):
    return render(request, 'index.html',{'nbar': 'home'})

def map(request):
    return render(request, 'interativeMap.html', {'nbar': 'map'})

def collection(request):
    return render(request, 'collection.html', {'nbar': 'collection'})

def AtoM_API_CALL(request,id):
    connection = client.HTTPConnection(ATOM_LOC)
    connection.request('GET', '/api/informationobjects/creeping-jane-trail',headers={'REST-API-Key': API_KEY})
    response = connection.getresponse()
    js = json.loads(response.read())
    music = urlparse("http://"+js["digital_object"]["reference_url"])._replace(netloc=ATOM_LOC).geturl()

    connection.request('GET', '/api/informationobjects/creeping-jane', headers={'REST-API-Key': API_KEY})
    response = connection.getresponse()
    js = json.loads(response.read())
    pdf = urlparse("http://" + js["digital_object"]["url"])._replace(netloc=ATOM_LOC).geturl()
    img = urlparse("http://" + js["digital_object"]["reference_url"])._replace(netloc=ATOM_LOC).geturl()


    return render(request, 'detail.html', {'nbar': 'collection', 'content': music, 'pdf':pdf ,'img':img})
