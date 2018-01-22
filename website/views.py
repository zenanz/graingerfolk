from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate,login
from website.form import RegistrationForm, ProfileForm, UserForm
from http import client
from urllib.parse import urlparse, urlsplit, urlunsplit
import json

# Create your views here.

ATOM_LOC = "10.100.148.152"
API_KEY = '799cbb5aae706a3a'


def dump_json(target):
    print(json.dumps(target, indent=4))


def correct_loc(target):
    u = list(urlsplit("http://" + target))
    u[1] = ATOM_LOC
    u = urlunsplit(u)
    return u


def search_AtoM(keyword='',skip=0):
    connection = client.HTTPConnection(ATOM_LOC)
    query = '/api/informationobjects?' +'skip='+str(skip)
    if keyword != '':
        query += '&sq0=' + keyword
    connection.request('GET', query, headers={'REST-API-Key': API_KEY})
    print('AtoM Request: ',query)
    response = connection.getresponse()
    return json.loads(response.read())


def index(request):
    return render(request, 'index.html', {'nbar': 'home'})


def map(request):
    return render(request, 'interativeMap.html', {'nbar': 'map'})


def collection(request):
    return render(request, 'collection.html', {'nbar': 'collection'})


def AtoM_API_CALL(request, description):
    connection = client.HTTPConnection(ATOM_LOC)
    connection.request('GET', '/api/informationobjects/' + description + '-trail', headers={'REST-API-Key': API_KEY})
    response = connection.getresponse()
    js = json.loads(response.read())
    music = urlparse("http://" + js["digital_object"]["reference_url"])._replace(netloc=ATOM_LOC).geturl()

    connection.request('GET', '/api/informationobjects/' + description, headers={'REST-API-Key': API_KEY})
    response = connection.getresponse()
    js = json.loads(response.read())
    pdf = urlparse("http://" + js["digital_object"]["url"])._replace(netloc=ATOM_LOC).geturl()
    img = urlparse("http://" + js["digital_object"]["reference_url"])._replace(netloc=ATOM_LOC).geturl()

    return render(request, 'detail.html', {'nbar': 'collection', 'content': music, 'pdf': pdf, 'img': img})


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'registration/signup.html', {'nbar': 'home' , 'form': form})

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            uform = UserForm(request.POST,instance=request.user)
            pform = ProfileForm(request.POST,request.FILES,instance=request.user.userprofile)
            if pform.is_valid() and uform.is_valid:

                pform.save()
                print(pform)

                uform.save()
                return redirect('profile')
        else:
            pform = ProfileForm()
            uform = UserForm()

        return  render(request, 'registration/profile.html', {'nbar': 'home', 'sidebar':'profile', 'pform': pform, 'uform':uform})
    else:
        return redirect('login')

def search(request):
    kw = request.POST.get('keyword')
    print(kw)
    result = search_AtoM(keyword=kw)
    #dump_json(result)
    objects = list(result['results'])
    for item in objects:
        if 'thumbnail_url' in item:
            thumbnail = item['thumbnail_url']
            item['thumbnail_url'] = correct_loc(thumbnail)
    return render(request, 'album.html', {'nbar': 'collection', 'results': objects, 'placeholder': kw,})

def load(request):
    kw = request.POST.get('keyword')
    skip = request.POST.get('skip')
    print(request.body)
    result = search_AtoM(keyword=kw,skip=int(skip)*10)
    for item in result['results']:
        if 'thumbnail_url' in item:
            thumbnail = item['thumbnail_url']
            item['thumbnail_url'] = correct_loc(thumbnail)
    #dump_json(result)

    return JsonResponse(result)

