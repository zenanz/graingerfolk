from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('interativeMap', views.map, name='map'),
    path('collection', views.collection, name='collection'),
    path('signup',views.signup),
    path('collection/detail/<slug:description>/', views.AtoM_API_CALL),
    path('collection/load/', views.load),
    path('collection/search/', views.search),
]