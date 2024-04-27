# src/app/shop/views.py

# Django and third party modules
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world_view(request):
	return HttpResponse("Hello World!")
