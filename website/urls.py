from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('interativeMap', views.map, name='map'),
    path('collection', views.collection, name='collection'),
    path('accounts/signup',views.signup),
    path('accounts/profile',views.profile, name='profile'),
    path('accounts/favorites',views.favorites, name='favorites'),
    path('accounts/password_change/', views.change_password, name='password_chagne'),
    path('collection/detail/<slug:description>/', views.AtoM_API_CALL),
    path('collection/load/', views.load),
    path('collection/search/', views.search),
    path('collection/favorites/',views.addFavorite, name='addFavorites'),
    path('accounts/', include('django.contrib.auth.urls')),
]