from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<str:name>', views.list_product),
    path('computer/', views.computer),
    path('smartphon/', views.smartphon),
]