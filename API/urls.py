
from django.urls import path
from . import views
from .views import*

urlpatterns = [
    path("academicien/", get_academicien, name="get_academiecien"),

]