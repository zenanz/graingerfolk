from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html',{'nbar': 'home'})

def map(request):
    return render(request, 'interativeMap.html', {'nbar': 'map'})

def collection(request):
    return render(request, 'collection.html', {'nbar': 'collection'})