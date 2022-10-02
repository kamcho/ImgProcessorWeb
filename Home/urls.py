from django.contrib import admin
from django.urls import path
# from notebook import view
from .views import *
from .views import Upload
from . import views
urlpatterns = [
    path('',Upload.as_view(),name='home'),
    path('mylib/',views.mylib,name='mylib'),
    path('success/',views.img,name='success'),
]