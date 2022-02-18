from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PersonaSerializers
from .models import Persona
from django.http import HttpResponse
# Create your views here.
def hola(request):
    return HttpResponse('<h1>HOLA</h1>')

class PersonaViewsets(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializers
