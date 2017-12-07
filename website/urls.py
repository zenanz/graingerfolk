from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^interativeMap$', views.map, name='map'),
    url(r'^collection$', views.collection, name='collection'),
]