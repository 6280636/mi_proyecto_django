from django.shortcuts import render
from django.http import HttpResponse
from .models import Mensaje

def mostrar_mensaje(request):
    m = Mensaje(texto="Hola, este es un mensaje de prueba")
    return HttpResponse(m.texto)

# Create your views here.
