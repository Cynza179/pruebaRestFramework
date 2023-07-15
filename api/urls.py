from django.urls import path,include
from rest_framework import routers  #administra rutas#
from api import views

ruta=routers.DefaultRouter()
ruta.register('profesor',views.ProfesorViewSet)

urlpatterns = [
    path('',include(ruta.urls)) 
]


