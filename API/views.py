from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def get_academicien(request):
    
    return JsonResponse(data={"success":True})
