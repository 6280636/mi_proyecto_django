from django.shortcuts import render
from django.http import HttpResponse
from .models import Mensaje
from datetime import datetime

def mostrar_mensaje(request):
    ahora = datetime.now().strftime("%H:%M:%S")
    return HttpResponse(f"<h1>Hora actual: {ahora}</h1><p>Esta es la rama de prueba hora.</p>")
# Create your views here.
