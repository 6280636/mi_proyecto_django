from django.shortcuts import render
from django.http import HttpResponse
from .models import Mensaje
from datetime import datetime

def mostrar_mensaje(request):   
    return HttpResponse("<h1>Mensaje desde rama A</h1>")
# Create your views here.
