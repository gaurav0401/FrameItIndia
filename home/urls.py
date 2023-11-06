from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name="index"),
    # path('addimages', views.addImages , name="addimages"),
    
]
