from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('destinations', views.destinations, name='destinations'),
    ###path('login', views.login, name='login'),
    ##path('logout', views.logout, name='logout')
    ]
