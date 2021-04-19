from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('city', views.city, name='city'),
    ###path('login', views.login, name='login'),
    ##path('logout', views.logout, name='logout')
    ]
