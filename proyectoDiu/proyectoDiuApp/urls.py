from re import template
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [

 path('', views.home, name = "home"),
 path('signup/', views.signup, name='signup'),
 path('information', views.information, name='information'),
 path('inicioUsr/', views.inicioUsr, name="inicioUsr"),
 path('inicioAdmin/', views.inicioAdmin, name="inicioAdmin"),
 path('deleteUser/', views.deleteUser, name="deleteUser"),
 path('deleteUser/eliminarUsuario/<email>', views.eliminarUsuario),
 path('add_cita',views.add_cita,name="add_cita"),
 path('delete_cita_menu/<cita_id>',views.delete_cita_menu,name="delete_cita_menu"),
 path('delete_cita/<cita_id>',views.delete_cita,name="delete_cita"),
 path('update_cita/<cita_id>',views.update_cita,name="update_cita"),
]+ static(settings.STATIC_URL)
