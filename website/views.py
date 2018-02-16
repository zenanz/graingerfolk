from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.db.models import Count
from website.form import RegistrationForm, ProfileForm, UserForm
from website.models import *
from http import client
from urllib.parse import urlparse, urlsplit, urlunsplit
import json
from graingerfolk.settings import ALLOWED_HOSTS

# Create your views here.

ATOM_LOC = "128.250.57.12"
API_KEY = '799cbb5aae706a3a'
HOST_LOC = ALLOWED_HOSTS[1]+":8000"

def dump_json(target):
    print(json.dumps(target, indent=4))


def correct_loc(target):
    u = list(urlsplit("http://" + target))
    u[1] = ATOM_LOC
    u = urlunsplit(u)
    return u


def search_AtoM(keyword='', skip=0):
    connection = client.HTTPConnection(ATOM_LOC)
    query = '/api/informationobjects?onlyMedia=1&' + 'skip=' + str(skip)
    if keyword is not None and keyword != '' :
        query += '&sq0=' + str(keyword)
    connection.request('GET', query, headers={'REST-API-Key': API_KEY})
    print('AtoM Request: ', query)
    response = connection.getresponse()
    return json.loads(response.read())


def retrieve_AtoM(slug):
    connection = client.HTTPConnection(ATOM_LOC)
    query = '/api/informationobjects/' + slug
    connection.request('GET', query, headers={'REST-API-Key': API_KEY})
    print('AtoM Request: ', query)
    response = connection.getresponse()
    return json.loads(response.read())


def index(request):
    return render(request, 'index.html', {'nbar': 'home'})


def map(request):
    return render(request, 'interativeMap.html', {'nbar': 'map'})


def collection(request):
    return render(request, 'collection.html', {'nbar': 'collection'})


def detail(request, description):
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

    comments = Comment.objects.filter(slug=description).annotate(number_of_likes=Count('like'))
    top_comments = comments.order_by('-number_of_likes').all()[:3]

    return render(request, 'detail.html',
                  {'nbar': 'collection',
                   'content': music,
                   'pdf': pdf, 'img': img,
                   'slug':description,
                   'comments':comments,
                   'host': HOST_LOC,
                   'top_comments': top_comments})


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

    return render(request, 'registration/signup.html', {'nbar': 'home', 'form': form})


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            uform = UserForm(request.POST, instance=request.user)
            pform = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

            if pform.is_valid() and uform.is_valid:
                uform.save()
                pform.save()


                return redirect('profile')
        else:
            pform = ProfileForm(instance=request.user.userprofile)
            uform = UserForm(instance=request.user)

        return render(request, 'registration/profile.html',
                      {'nbar': 'home', 'sidebar': 'profile', 'pform': pform, 'uform': uform})
    else:
        return redirect('login')

def setting(request):
    return render(request, 'registration/setting.html', {'nbar': 'home', 'sidebar': 'setting',})


def favorites(request):
    if request.user.is_authenticated:
        kw = request.GET.get('keyword')
        order_date = request.GET.get('date-added')
        if order_date is None or order_date == '':
            order_date = '-date_added'
        print(order_date)
        favs = []
        if kw != '' and kw is not None:
            favs_objs = Favourites.objects.filter(user=request.user,title__icontains=kw).order_by(order_date).all()
        else:
            favs_objs = Favourites.objects.filter(user=request.user).order_by(order_date).all()
        for item in favs_objs:
            favs.append({'slug': item.slug, 'detail': json.loads(item.detail)})

        return render(request, 'registration/favorites.html',
                      {'nbar': 'home', 'sidebar': 'favorites', 'favs': favs, 'kw': kw, 'host': HOST_LOC})
    else:
        return redirect('login')


def search(request):
    kw = request.GET.get('keyword')
    print(kw)
    result = search_AtoM(keyword=kw)
    # dump_json(result)
    objects = list(result['results'])
    favs_slug = []
    for item in objects:
        if 'thumbnail_url' in item:
            thumbnail = item['thumbnail_url']
            item['thumbnail_url'] = correct_loc(thumbnail)

    if request.user.is_authenticated:
        favs = Favourites.objects.filter(user=request.user).all()
        for object in favs:
            favs_slug.append(object.slug)
    return render(request, 'album.html', {'nbar': 'collection', 'results': objects, 'placeholder': kw, 'favs': favs_slug, 'host': HOST_LOC})


def load(request):
    kw = request.POST.get('keyword')
    skip = request.POST.get('skip')
    print(request.body)
    result = search_AtoM(keyword=kw, skip=int(skip) * 10)
    for item in result['results']:
        if 'thumbnail_url' in item:
            thumbnail = item['thumbnail_url']
            item['thumbnail_url'] = correct_loc(thumbnail)
    # dump_json(result)

    return JsonResponse(result)


def addFavorite(request):
    if request.user.is_authenticated:
        kw = request.POST.get('keyword')
        print(request.body)
        result = retrieve_AtoM(kw)
        record = Favourites.objects.filter(slug=kw).first()
        if record is None:
            if result.get('digital_object'):
                if result.get('digital_object').get('thumbnail_url'):
                    result['digital_object']['thumbnail_url'] = correct_loc(result['digital_object']['thumbnail_url'])
            newFavorite = Favourites(slug=kw, user=request.user, title=result.get('title'), detail=json.dumps(result))
            newFavorite.save()
        else:
            record.delete()
        return HttpResponse(200)
    else:
        return HttpResponse(401)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
            return render(request, 'registration/password_change.html', {
                'form': form
            })
    else:
        if request.user.is_authenticated:
            form = PasswordChangeForm(request.user)
            return render(request, 'registration/password_change.html', {
                'form': form
            })
        else:
            return redirect('login')

def comment(request,description):
    if request.user.is_authenticated:
        content = request.POST.get('comment')
        cid = request.POST.get('cid')
        recipient = request.POST.get('recipient')
        next_loc = request.POST.get('next', '/')
        print (recipient, cid, content, )
        if cid is not None and cid !='':
            parent = Comment.objects.get(id=cid)
            new_comment = Comment(slug=description, user=request.user, content=content+'//@'+parent.user.username+': '+parent.content, parent=parent)
        else:
            new_comment = Comment(slug=description, user=request.user, content=content)
        new_comment.save()
        return redirect(next_loc)
    else:
        return redirect('login')

def like(request, cid):
    if request.user.is_authenticated:
        print(cid, request.user.id)
        cmt = Comment.objects.get(id=cid)
        if request.user in cmt.like.all():
            print('in')
            cmt.like.remove(request.user)
        else:
            print('out')
            cmt.like.add(request.user)
        count = cmt.like.all().count()
        return JsonResponse({'count': count})
    else:
        return HttpResponse(403)