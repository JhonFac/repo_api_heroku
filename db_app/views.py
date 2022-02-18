from django.shortcuts import render
# from rest_framework import viewsets
from .serializers import Model_FormsSerializers
from .models import Model_Forms
from django.views import View
from .models import Model_Forms
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from db_app import api_ss
import json
import requests


class RequesForms(View):
    def get(self, request):
        return HttpResponse('<h1>pagina en blanco</h1>')

class GetData(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)


    def post(self, request):

        data=json.loads(request.body) 
        response = api_ss.SendDataSharpSpring().SendData(request.body)

        return JsonResponse(response)
