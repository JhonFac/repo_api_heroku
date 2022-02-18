from django.shortcuts import render
# from rest_framework import viewsets
from .serializers import Model_FormsSerializers
from .models import Model_Forms
from django.views import View
from .models import Model_Forms
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# Create your views here.  
def hola(request):
    return HttpResponse('<h1>HOLA</h1>')

# class PersonaViewsets(viewsets.ModelViewSet):
#     queryset = Persona.objects.all()
#     serializer_class = PersonaSerializers

class RequesForms(View):
    def get(self, request):
        return HttpResponse('<h1>siiii</h1>')

        # Clist= Model_Forms.objects.all()
        # return JsonResponse(list(Clist.values()), safe=False)

# class GetData(viewsets):

#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs) :
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request):

#         data=json.loads(request.body) 
#         response = api_ss.SendDataSharpSpring().SendData(request.body)

#         return JsonResponse(response)