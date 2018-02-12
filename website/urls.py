from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import password_reset
from . import views
from .form import EmailValidationOnForgotPassword
import django

urlpatterns = [
    path('', views.index, name='index'),
    path('interativeMap', views.map, name='map'),
    path('collection', views.collection, name='collection'),
    path('accounts/signup', views.signup),
    path('accounts/profile', views.profile, name='profile'),
    path('accounts/setting', views.setting, name='setting'),
    path('accounts/favorites', views.favorites, name='favorites'),
    path('accounts/password_change/', views.change_password, name='change_password'),
    path('collection/detail/<slug:description>/', views.detail, name='detail'),
    path('collection/comment/<slug:description>/', views.comment, name='detail'),
    path('collection/comment/like/<int:cid>/', views.like, name='like'),
    path('collection/load/', views.load),
    path('collection/search/', views.search),
    path('collection/favorites/', views.addFavorite, name='addFavorites'),
    path('accounts/password_reset/',
        password_reset,
        {'post_reset_redirect': '/accounts/password_reset/done/',
         'html_email_template_name': 'registration/password_reset_email.html',
         'password_reset_form': EmailValidationOnForgotPassword},
        name="password_reset"),
    path('accounts/', include('django.contrib.auth.urls')),
]
