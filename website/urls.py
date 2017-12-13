from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('interativeMap', views.map, name='map'),
    path('collection', views.collection, name='collection'),
    path('collection/detail/<int:id>/', views.AtoM_API_CALL),
]