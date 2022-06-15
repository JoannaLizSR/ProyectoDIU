
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from proyectoDiuApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('proyectoDiuApp.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='vistas/password_reset_done.html'), 			name='password_reset_done'),
 path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="vistas/password_reset_confirm.html"), name='password_reset_confirm'),
 path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='vistas/password_reset_complete.html'), name='password_reset_complete'),    
 path("password_reset/", views.password_reset_request, name="password_reset"),



]+ static(settings.STATIC_URL)
