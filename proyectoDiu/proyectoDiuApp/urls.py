from re import template
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [

 path('', views.home, name = "home"),
 path('signup/', views.signup, name='signup'),
 path('information', views.information, name='information'),
 path('inicioUsr/', views.inicioUsr, name="inicioUsr"),
 path('inicioAdmin/', views.inicioAdmin, name="inicioAdmin"),
 path('deleteUser/', views.deleteUser, name="deleteUser"),
]
