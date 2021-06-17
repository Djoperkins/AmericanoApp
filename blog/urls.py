from blog import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('home/header/', views.home, name='header'),
    path('home/intro/', views.home, name='intro'),
    path('home/services/', views.home, name='services'),
    path('home/audio', views.home, name='audio'),
    path('home/callMe', views.home, name='callMe'),
    path('home/projects', views.home, name='projects'),
    path('home/about', views.home, name='about'),
    path('home/contact', views.home, name='contact'),

    path('all_actus/', views.all_actus, name='all_actus'),
    path('all_videos/', views.all_videos, name='all_videos'),
    path('all_photos/', views.all_photos, name='all_photos'),
    path('all_albums/', views.all_albums, name='all_albums'),
]
